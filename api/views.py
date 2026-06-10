from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Products
from .serializer import PrdSer
from rest_framework.status import HTTP_200_OK
# Create your views here.
class ProductApi(APIView):
    def get(self,request):
        prds = Products.objects.all()#python query set
        #needs to convert to json so we use serialisation
        #two types we have
        #normal serialisaiton,model serialisation
        serialise_obj = PrdSer(prds,many=True)#contains json obj
        return Response(serialise_obj.data,status=HTTP_200_OK)