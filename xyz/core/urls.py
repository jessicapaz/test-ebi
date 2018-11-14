from django.urls import path
from .views import SellerViewSet
from .views import ClientViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('seller', SellerViewSet, base_name='seller')
router.register('client', ClientViewSet, base_name='client')
urlpatterns = []
urlpatterns += router.urls
