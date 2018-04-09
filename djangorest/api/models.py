from django.db import models

class Bucketlist(models.Model):

    name = models.CharField(max_length=255, blank=False, unique=True)
    owner = models.ForeignKey('auth.user',
    related_name='bucketlists',
    on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        #return a human readable representation of the model instance
        return "{}".format(self.name)
