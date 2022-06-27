from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication

from customers.models import Customer
from users.permissions import IsRequester
from ..serializers import CustomerSerializer


class CustomerListAPIView(ListAPIView):
    permission_classes = (IsRequester,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = PageNumberPagination
