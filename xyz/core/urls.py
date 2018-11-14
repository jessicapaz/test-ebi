from django.urls import path
from .views import SellerViewSet
from .views import ClientViewSet
from .views import ProductServiceView
from .views import SaleView
from .views import SellerCommissionView
from .views import ClientProductsView
from .views import TopProductsView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('seller', SellerViewSet, base_name='seller')
router.register('client', ClientViewSet, base_name='client')
urlpatterns = [
    path('product-service/',
        ProductServiceView.as_view(),
        name='product-service'
    ),
    path('sale/',
        SaleView.as_view(),
        name='sale'
    ),
    path('total-commission/',
        SellerCommissionView.as_view(),
        name='total-commission'
    ),
    path('client-most-products/',
        ClientProductsView.as_view(),
        name='client-most-products'
    ),
    path('top-products/',
        TopProductsView.as_view(),
        name='top-products'
    ),
]

urlpatterns += router.urls
