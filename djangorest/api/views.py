from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

class CreateView(generics.ListCreateAPIView): # The ListCreateAPIView is a generic
                                            # view which provides GET (list all) and POST method handlers
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        # save the post data when creating a new bucketlist
        serializer.save()

# this class defines the create behaviour of our rest api

#RetrieveUpdateDestroyAPIView is a generic view that provides GET(one),
#PUT, PATCH and DELETE method handlers.

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    # This class handles the http GET, PUT and DELETE requests
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
