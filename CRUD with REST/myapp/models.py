from django.db import models
from datetime import datetime

# Create your models here.
class Bucketlist(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(default=datetime.now)
    technology = models.ManyToManyField('Tech')


    def __str__(self):
        return self.name

class User(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    bucket_id = models.ForeignKey('Bucketlist',on_delete=models.CASCADE)

    def __str__(self):
        return self.user_name

class Tech(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
