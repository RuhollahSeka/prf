from rest_framework import serializers

from products.api.v1.serializers import ProductSerializer
from product_requests.models import ProductRequestItem


class ProductRequestItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = ProductRequestItem
        fields = (
            'id',
            'product',
            'quantity',
            'expiry_date',
            'note',
        )
