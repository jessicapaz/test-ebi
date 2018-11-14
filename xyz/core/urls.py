from django.urls import path
from .views import SellerViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('seller', SellerViewSet, base_name='seller')
urlpatterns = [
]
urlpatterns += router.urls
