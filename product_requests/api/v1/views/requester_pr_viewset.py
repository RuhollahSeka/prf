from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from product_requests.models import ProductRequest
from users.permissions import IsRequester
from ..filters import ProductRequestFilter
from ..serializers import ProductRequestEditSerializer, ProductRequestListSerializer


class RequesterPRViewset(ModelViewSet):
    permission_classes = (IsRequester,)
    authentication_classes = (JWTAuthentication,)
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_class = ProductRequestFilter
    search_fields = ('customer__name',)
    ordering_fields = ('created', 'earliest_expected_date')
    ordering = ('-created',)
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action.lower() == 'list':
            return ProductRequestListSerializer
        return ProductRequestEditSerializer

    def get_queryset(self):
        user = self.request.user
        return ProductRequest.objects.filter(requester=user)
