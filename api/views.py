from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from product.models import Products
from .serializer import PrdSer,UserSerializer
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST,HTTP_201_CREATED,HTTP_404_NOT_FOUND
from django.http import Http404
from django.shortcuts import get_object_or_404
from .serializer import CustomProductSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.generics import ListCreateAPIView
# Create your views here.
class ProductApi(APIView):
    authentication_classes = [JWTAuthentication] #adding the authentication uses
    #permission_classes = [IsAuthenticated]#whether user logged oin or not
    permission_classes = [IsAdminUser]#whether admin user logged oin or not
    def get(self,request):
        prds = Products.objects.all()#python query set
        #needs to convert to json so we use serialisation
        #two types we have
        #normal serialisaiton,model serialisation
        paginator = PageNumberPagination()
        paginator.page_size = 3
        pages = paginator.paginate_queryset(prds,request)
        serialise_obj = PrdSer(pages,many=True)#contains json obj
        return paginator.get_paginated_response(serialise_obj.data)
    
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
        
class ModifyCustomProductApi(APIView):
    def get(self,request,pk):
        prds = get_object_or_404(Products,id=pk)
        s_obj = PrdSer(prds)
        return Response(s_obj.data,status=HTTP_200_OK)

    def put(self,request,pk):
        prds = get_object_or_404(Products,id=pk)
        s_obj = CustomProductSerializer(prds,data=request.data)
        if s_obj.is_valid()==True:
            s_obj.save()
            return Response(s_obj.data,status=HTTP_200_OK)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)


class ProductsViewSet(ViewSet):
    def list(self,request):
        prd = Products.objects.all()
        s_obj = PrdSer(prd,many=True)
        return Response(s_obj.data,status=HTTP_200_OK)
    def create(self,request):
        s_obj = PrdSer(data=request.data)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        prd = get_object_or_404(Products,id=pk)
        s_obj = PrdSer(prd,data=request.data,partial=True)
        if s_obj.is_valid() == True:
            s_obj.save()
            return Response(s_obj.data,status=HTTP_200_OK)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
    def destroy(self,request,pk):
        prd = get_object_or_404(Products,id=pk)
        prd.delete()
        return Response(status=HTTP_200_OK)
    def retrieve(self,request,pk):
        prd = get_object_or_404(Products,id=pk)
        s_obj = PrdSer(prd)
        return Response(s_obj.data,status=HTTP_200_OK)
    
class UserRegisterView(APIView):
    def get(self,request):
        return Response(status=HTTP_200_OK)
    def post(self,request):
        s_obj = UserSerializer(data=request.data)
        if s_obj.is_valid() == True:
            u_obj = s_obj.save()#saving in serialiser object
            u_obj.set_password(s_obj.validated_data['password'])
            u_obj.save()#saving in db tbale data

            return Response(status=HTTP_201_CREATED)
        else:
            return Response(s_obj.errors,status=HTTP_400_BAD_REQUEST)
        
class GenericProductApi(ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = PrdSer