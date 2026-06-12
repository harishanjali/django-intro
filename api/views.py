from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Products
from .serializer import PrdSer
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_404_NOT_FOUND
from django.http import Http404
from django.shortcuts import get_object_or_404
from .serializer import CustomProductSerializer
# Create your views here.
class ProductApi(APIView):
    def get(self,request):
        prds = Products.objects.all()#python query set
        #needs to convert to json so we use serialisation
        #two types we have
        #normal serialisaiton,model serialisation
        serialise_obj = PrdSer(prds,many=True)#contains json obj
        return Response(serialise_obj.data,status=HTTP_200_OK)
    
    def post(self,request):
        s_obj = PrdSer(data=request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)

class UpdateProductApi(APIView):
    def get_product(self,pk):
        return get_object_or_404(Products,id=pk)
    def get(self,request,pk):
        product = self.get_product(pk)
        s_obj = PrdSer(product)
        return Response(s_obj.data,status=HTTP_200_OK)
    def put(self,request,pk):
        prd = self.get_product(pk)
        s_obj = PrdSer(prd,request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        prd = self.get_product(pk)
        prd.delete()
        return Response(status=HTTP_200_OK)
    
class CustomProductApi(APIView):
    def get(self,request):
        return Response(status=HTTP_200_OK)
    def post(self,request):
        s_obj = CustomProductSerializer(data=request.data)
        if s_obj.is_valid():
            s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST )