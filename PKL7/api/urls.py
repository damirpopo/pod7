from django.urls import path, include, re_path
from .views import *

urlpatterns = [
    path('cart/', CartList.as_view()),
    path('cart/<int:pk>/', CartUpdate.as_view()),
    path('cartdel/<int:pk>/', CartDestroy.as_view()),
    path('product/', ProductList.as_view()),
    path('product/<int:pk>/', ProductUpdate.as_view()),
    path('productdel/<int:pk>/', ProductDestroy.as_view()),
    path('order/', OrderList.as_view()),
    path('order/<int:pk>/', OrderUpdate.as_view()),
    path('orderdel/<int:pk>/', OrderDestroy.as_view()),
    path('auth2/', include('djoser.urls')),
    re_path(r'^auth2/', include('djoser.urls.authtoken'))
]