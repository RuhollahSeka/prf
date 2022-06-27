from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from product_requests.models import ProductRequest
from users.permissions import IsFulfiller
from ..filters import ProductRequestFilter
from ..serializers import ProductRequestListSerializer, ProductRequestStatusEditSerializer


class FulfillerPRViewset(ModelViewSet):
    permission_classes = (IsFulfiller,)
    authentication_classes = (JWTAuthentication,)
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductRequestFilter
    search_fields = ('customer__name', 'requester__first_name')
    ordering_fields = ('created', 'earliest_expected_date')
    ordering = ('-created',)
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action.lower() == 'list':
            return ProductRequestListSerializer
        return ProductRequestStatusEditSerializer

    def get_queryset(self):
        valid_statuses = [ProductRequest.STATUS_PENDING, ProductRequest.STATUS_FULFILLED]
        return ProductRequest.objects.filter(status__in=valid_statuses)
