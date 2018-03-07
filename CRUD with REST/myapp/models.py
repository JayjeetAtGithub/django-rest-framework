from django.db import models
from datetime import datetime

# Create your models here.
class Bucketlist(models.Model):
    name = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=datetime.now)
    date_modified = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
