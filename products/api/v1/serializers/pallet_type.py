from rest_framework import serializers

from products.models import PalletType


class PalletTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PalletType
        fields = (
            'id',
            'name',
        )
