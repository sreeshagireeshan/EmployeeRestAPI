
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmployeeDetailsSerializers
from .models import *
from django.http import JsonResponse
# Create your views here.

class EmployeeDetailsViews(APIView):
     def post(self,request):
        serializer = EmployeeDetailsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({"status":"error","data":serializer.errors},status=status.HTTP_400_BAD)

    # def get(self,request,id=None):
       # if id:
           # item = EmployeeDetails.objects.get(id=id)
           # serializer = EmployeeDetailsSerializers(item)
            #return JsonResponse({"status":"success","data":serializer.data},status=status.HTTP_200_OK)
          
     def get(self,request,id=None):
          if id:
               item=EmployeeDetails.objects.get(id=id)
               serializer=EmployeeDetailsSerializers(item)
               return JsonResponse({"status": "success","data":serializer.data},status=status.HTTP_200_OK) 
            
          items=EmployeeDetails.objects.all()
          serializer=EmployeeDetailsSerializers(items,many=True)
        
          return JsonResponse({"status": "success","data":serializer.data},status=status.HTTP_200_OK)

     def put(self,request,id=None):
        if id:
             item=EmployeeDetails.objects.get(id=id)
             serializer=EmployeeDetailsSerializers(item,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status":" put is success","data":serializer.data})
        else:
            return Response({"status":"error","data":serializer.errors})

     def delete(self,request,id=None):
        item=EmployeeDetails.objects.get(id=id)
        item.delete()
        return Response({"status":"success","data":"itemdeleted"})
   
