from rest_framework import serializers

from products.api.v1.serializers import VariantSerializer
from product_requests.models import ProductRequestItem


class ProductRequestItemSerializer(serializers.ModelSerializer):
    product = VariantSerializer(read_only=True)

    class Meta:
        model = ProductRequestItem
        fields = (
            'id',
            'variant',
            'quantity',
            'expiry_date',
            'note',
        )
