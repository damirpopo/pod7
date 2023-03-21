from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView
from .models import Order,Product,Cart
from rest_framework.authentication import TokenAuthentication
from .serializers import Cartserializer,Productserializer,Orderserializer
from .permission import ReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly



class CartList(ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = Cartserializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CartUpdate(RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Cartserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CartDestroy(RetrieveDestroyAPIView):
    queryset = Cart.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Cartserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = Productserializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (ReadOnly,)


class ProductUpdate(RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Productserializer
    permission_classes = (ReadOnly,)

class ProductDestroy(RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Productserializer
    permission_classes = (ReadOnly,)

class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = Orderserializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OrderUpdate(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Orderserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class OrderDestroy(RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    authentication_classes = (TokenAuthentication,)
    serializer_class = Orderserializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
