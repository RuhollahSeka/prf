from rest_framework import serializers

from customers.api.v1.serializers import CustomerSerializer, CustomerAddressSerializer
from products.api.v1.serializers import PalletTypeSerializer, ShrinkWrapSerializer
from product_requests.models import ProductRequest
from users.api.v1.serializers import UserSerializer


class ProductRequestListSerializer(serializers.ModelSerializer):
    requester = UserSerializer(read_only=True)
    customer = CustomerSerializer(read_only=True)
    address = CustomerAddressSerializer(read_only=True)
    pallet_type = PalletTypeSerializer(read_only=True)
    shrink_wrap = ShrinkWrapSerializer(read_only=True)

    class Meta:
        model = ProductRequest
        fields = (
            'id',
            'created',
            'updated',
            'requester',
            'type',
            'customer',
            'address',
            'needs_address_label',
            'status',
            'earliest_expected_date',
            'pallet_type',
            'shrink_wrap',
            'special_instructions',
        )
