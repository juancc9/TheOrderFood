from rest_framework.routers import DefaultRouter
from .views import ProductViewset, OrdenViewset

router = DefaultRouter()
router.register(prefix='products',viewset=ProductViewset)
router.register(prefix='ordenes',viewset=OrdenViewset)