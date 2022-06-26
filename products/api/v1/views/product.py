from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import Product
from users.permissions import IsRequester
from ..serializers import ProductSerializer


class ProductListAPIView(ListAPIView):
    permission_classes = (IsRequester,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = ProductSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('code',)
    queryset = Product.objects.all()
