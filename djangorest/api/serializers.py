#Serializing is changing the data from complex query sets from the db, to a form
#of data we can understand like JSON or XML.

from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    #maps the Model instwance into JSON format

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        #Meta class to map serializers fields with the model fields
        model = Bucketlist
        fields = ('id', 'name', 'owner','date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
