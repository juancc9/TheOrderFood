from rest_framework.serializers import ModelSerializer
from apps.products.models import Product, Orden

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'


class OrdenSerializer(ModelSerializer):
    class Meta:
        model = Orden
        fields = '__all__' 