from django.urls import path
from .views import SellerViewSet
from .views import ClientViewSet
from .views import ProductServiceListView
from .views import ProductServiceDetailView
from .views import SaleListView
from .views import SaleDetailView
from .views import SellerCommissionView
from .views import ClientProductsView
from .views import MostSoldView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('seller', SellerViewSet, base_name='seller')
router.register('client', ClientViewSet, base_name='client')
urlpatterns = [
    path('product-service/',
        ProductServiceListView.as_view(),
        name='product-service'
    ),
    path('product-service/<slug:pk>',
        ProductServiceDetailView.as_view(),
        name='product-service'
    ),
    path('sale/',
        SaleListView.as_view(),
        name='sale'
    ),
    path('sale/<slug:pk>',
        SaleDetailView.as_view(),
        name='sale'
    ),
    path('seller-commission/',
        SellerCommissionView.as_view(),
        name='seller-commission'
    ),
    path('client-most-sold/',
        ClientProductsView.as_view(),
        name='client-most-sold'
    ),
    path('most-sold/',
        MostSoldView.as_view(),
        name='most-sold'
    ),
]

urlpatterns += router.urls
