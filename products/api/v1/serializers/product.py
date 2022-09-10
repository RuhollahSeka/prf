from rest_framework import serializers

from products.models import Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = (
            'id',
            'name',
            'code',
        )
