from django.contrib import admin
from .models import Bucketlist,User,Tech
# Register your models here.
admin.site.register(Bucketlist)
admin.site.register(User)
admin.site.register(Tech)
