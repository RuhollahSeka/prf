from rest_framework import serializers

from customers.models import CustomerAddress


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
