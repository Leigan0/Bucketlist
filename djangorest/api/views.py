from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import BucketlistSerializer
from .models import Bucketlist
from .permissions import IsOwner

class CreateView(generics.ListCreateAPIView): # The ListCreateAPIView is a generic
                                            # view which provides GET (list all) and POST method handlers
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsOwner)

    #the permission class will deny permission to any unauthenticated user and
    # allow persmission otherwise

    def perform_create(self, serializer):
        # save the post data when creating a new bucketlist
        serializer.save(owner=self.request.user)

# this class defines the create behaviour of our rest api

#RetrieveUpdateDestroyAPIView is a generic view that provides GET(one),
#PUT, PATCH and DELETE method handlers.

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    # This class handles the http GET, PUT and DELETE requests
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner)
