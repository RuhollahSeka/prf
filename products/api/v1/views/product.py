from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from products.models import Variant
from users.permissions import IsRequester
from ..serializers import VariantSerializer


class VariantListAPIView(ListAPIView):
    permission_classes = (IsRequester,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = VariantSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('code',)
    queryset = Variant.objects.all()
    pagination_class = PageNumberPagination
