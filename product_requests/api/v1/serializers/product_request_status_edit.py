from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from customers.api.v1.serializers import CustomerSerializer, CustomerAddressSerializer
from product_requests.models import ProductRequest
from products.api.v1.serializers import PalletTypeSerializer, ShrinkWrapSerializer
from .job_readonly import JobReadOnlySerializer
from .product_request_item import ProductRequestItemSerializer


class ProductRequestStatusEditSerializer(serializers.ModelSerializer):
    items = ProductRequestItemSerializer(many=True, read_only=True)
    jobs = JobReadOnlySerializer(many=True, read_only=True)
    customer = CustomerSerializer(read_only=True)
    address = CustomerAddressSerializer(read_only=True)
    pallet_type = PalletTypeSerializer(read_only=True)
    shrink_wrap = ShrinkWrapSerializer(read_only=True)

    class Meta:
        model = ProductRequest
        fields = (
            'id',
            'type',
            'customer',
            'address',
            'needs_address_label',
            'status',
            'earliest_expected_date',
            'pallet_type',
            'shrink_wrap',
            'special_instructions',
            'items',
            'jobs',
        )
        read_only_fields = (
            'id',
            'type',
            'customer',
            'address',
            'needs_address_label',
            'pallet_type',
            'shrink_wrap',
            'special_instructions',
            'items',
            'jobs',
        )

    def validate(self, attrs):
        status = attrs['status']
        if status not in [ProductRequest.STATUS_FULFILLED, ProductRequest.STATUS_REJECTED]:
            raise ValidationError('Fulfiller can not set this status for a product request')
        return super().validate(attrs)
