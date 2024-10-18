from rest_framework.viewsets import ModelViewSet
from apps.products.models import Product, Orden
from apps.products.serializers import ProductSerializer,OrdenSerializer
from rest_framework.permissions import IsAuthenticated
from apps.products.api.permissions import Permiso

class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



class OrdenViewset(ModelViewSet):
    permission_classes = [Permiso]
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
    http_method_names = ['get','post','put']
        
    
