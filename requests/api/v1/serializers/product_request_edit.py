from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from requests.models import ProductRequest, ProductRequestItem
from .product_request_item import ProductRequestItemSerializer


class ProductRequestEditSerializer(serializers.ModelSerializer):
    items = ProductRequestItemSerializer(many=True, read_only=True)

    class Meta:
        model = ProductRequest
        fields = (
            'id',
            'customer',
            'address',
            'needs_address_label',
            'status',
            'earliest_expected_date',
            'pallet_type',
            'shrink_wrap',
            'special_instructions',
            'items',
        )
        read_only_fields = (
            'id',
            'items',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._items_data = None

    def to_internal_value(self, data):
        self._items_data = data.get('items')
        return super().to_internal_value(data)

    def validate(self, attrs):
        status = attrs['status']
        if status not in [ProductRequest.STATUS_DRAFT, ProductRequest.STATUS_CANCELLED, ProductRequest.STATUS_PENDING]:
            raise ValidationError('Requester can not set this status for a product request')
        return super().validate(attrs)

    def create_items(self, product_request):
        ProductRequestItem.objects.filter(product_request=product_request).delete()
        items_to_create = []
        for item_data in self._items_data:
            items_to_create.append(ProductRequestItem(
                product_request=product_request,
                product_id=item_data['product_id'],
                quantity=item_data['quantity'],
                expiry_date=item_data['expiry_date'],
                note=item_data['note'],
            ))
        ProductRequestItem.objects.bulk_create(items_to_create)

    def create(self, validated_data):
        validated_data['requester'] = self.context['request'].user
        with transaction.atomic():
            product_request = super().create(validated_data)
            self.create_items(product_request)
        return product_request
