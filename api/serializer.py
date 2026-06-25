from rest_framework.serializers import ModelSerializer
from product.models import Products
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
#serializer helps to convert the raw data into JSON and return the response
class PrdSer(ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'#['id','pname','pprice']

class CustomProductSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    pname = serializers.CharField(max_length=30)
    pprice = serializers.IntegerField()
    c_gst = serializers.IntegerField()
    s_gst = serializers.IntegerField()

    #our validations its method overrding
    def validate(self,validate_data):
        if validate_data['pprice']<0:
            raise ValidationError('Price should not negative')
        return validate_data


    def create(self,validate_data):
        # id = validate_data['id']
        pname = validate_data['pname']
        pprice = validate_data['pprice']
        c_gst = validate_data['c_gst']
        s_gst = validate_data['s_gst']
        p_obj = Products.objects.create(pname=pname,pprice=pprice+c_gst+s_gst)
        return p_obj
    
    def update(self,instance,validate_data):
        instance.pname = validate_data['pname']
        instance.pprice = validate_data['pprice']#+validate_data['c_gst']+validate_data['s_gst']
        instance.save()

        return instance
    
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']