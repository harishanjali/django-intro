from rest_framework.serializers import ModelSerializer
from product.models import Products

#serializer helps to convert the raw data into JSON and return the response
class PrdSer(ModelSerializer):
    class Meta:
        model = Products
        fields = ['id','pname','pprice']