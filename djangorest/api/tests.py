from django.test import TestCase
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
