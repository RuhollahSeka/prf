from rest_framework import serializers

from customers.models import Customer, CustomerAddress


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = (
            'id',
            'line1',
            'line2',
            'city',
            'country',
            'postal_code',
        )


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
