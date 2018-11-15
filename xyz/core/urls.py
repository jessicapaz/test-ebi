from django.urls import path
from .views import SellerViewSet
from .views import ClientViewSet
from .views import ProductServiceListView
from .views import ProductServiceDetailView
from .views import SaleListView
from .views import SaleDetailView
from .views import SellerCommissionView
from .views import ClientProductsView
from .views import MostSelledView
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('seller', SellerViewSet, base_name='seller')
router.register('client', ClientViewSet, base_name='client')
urlpatterns = [
    path('product-service/',
        ProductServiceListView.as_view(),
        name='product-service'
    ),
    path('product-service-detail/<slug:pk>',
        ProductServiceDetailView.as_view(),
        name='product-service-detail'
    ),
    path('sale/',
        SaleListView.as_view(),
        name='sale'
    ),
    path('sale-detail/<slug:pk>',
        SaleDetailView.as_view(),
        name='sale-detail'
    ),
    path('total-commission/',
        SellerCommissionView.as_view(),
        name='total-commission'
    ),
    path('client-most-products/',
        ClientProductsView.as_view(),
        name='client-most-products'
    ),
    path('most-selled/',
        MostSelledView.as_view(),
        name='most-selled'
    ),
]

urlpatterns += router.urls
