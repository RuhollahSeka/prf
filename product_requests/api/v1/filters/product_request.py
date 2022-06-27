import django_filters

from product_requests.models import ProductRequest


class ProductRequestFilter(django_filters.FilterSet):
    class Meta:
        model = ProductRequest
        fields = {
            'status': ['exact'],
            'pallet_type': ['exact'],
            'type': ['exact'],
        }
