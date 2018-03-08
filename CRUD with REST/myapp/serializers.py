from rest_framework import serializers
from .models import Bucketlist,User,Tech

class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tech
        fields = '__all__'
