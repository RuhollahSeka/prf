from rest_framework import serializers

from product_requests.models import Job
from products.api.v1.serializers import VariantSerializer
from users.api.v1.serializers import UserSerializer


class JobReadOnlySerializer(serializers.ModelSerializer):
    fulfiller = UserSerializer(read_only=True)
    product = VariantSerializer(read_only=True)

    class Meta:
        model = Job
        fields = (
            'id',
            'created',
            'fulfiller',
            'product',
            'quantity',
        )
