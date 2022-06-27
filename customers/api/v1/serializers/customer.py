from rest_framework import serializers

from customers.models import Customer
from .address import CustomerAddressSerializer


class CustomerSerializer(serializers.ModelSerializer):
    addresses = CustomerAddressSerializer(many=True, read_only=True)

    class Meta:
        model = Customer
        fields = (
            'id',
            'name',
            'country',
            'addresses',
        )
