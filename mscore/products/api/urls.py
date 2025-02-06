from django.urls import path

from products.api.views import ProductViewSet, UserApiView

urlpatterns = [
    path('products/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('users/', UserApiView.as_view())

]
