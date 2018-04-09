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
