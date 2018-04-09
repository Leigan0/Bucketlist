from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Bucketlist

class ModelTestCase(TestCase):
    #Tests for BucketList model

    def setUp(self):
        # Defines test client and test variables
        self.bucketlist_name = "Write a Django app"
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    #Test suite for the api views

    def setUp(self):
        #define the test client and other test variables
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to New York'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_bucketlist(self):
        #Test the api has bucket creation capability
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_bucket_list(self):
        #Test api can get a given bucketlist
        bucketlist = Bucketlist.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': bucketlist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)
