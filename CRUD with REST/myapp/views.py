from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bucketlist
from .serializers import BucketlistSerializer

# Create your views here.
class bucketlist(APIView):
    def get(self,request,format=None):
        blist = Bucketlist.objects.all()
        serializer = BucketlistSerializer(blist,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


class bucketdetail(APIView):
#this is a custom function not a PRE-DEFINED one
#--------------------------------------------------
    def get_object(self,pk):
        try:
            return Bucketlist.objects.get(pk=pk)
        except Bucketlist.DoesNotExist:
            raise Http404
#--------------------------------------------------
    def get(self,request,pk,format=None):
        bucket = self.get_object(pk)
        serializer = BucketlistSerializer(bucket)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        bucket = self.get_object(pk)
        serializer = BucketlistSerializer(bucket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bucket = self.get_object(pk)
        bucket.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
