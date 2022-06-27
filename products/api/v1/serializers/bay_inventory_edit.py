from rest_framework import serializers

from products.models import BayInventory


class BayInventoryEditSerializer(serializers.ModelSerializer):
    adjustment = serializers.IntegerField(write_only=True)

    class Meta:
        model = BayInventory
        fields = (
            'id',
            'product',
            'bay',
            'quantity',
            'adjustment',
        )
        read_only_fields = (
            'id',
            'product',
            'bay',
            'quantity',
        )

    def update(self, instance, validated_data):
        adjustment = validated_data.pop('adjustment', 0)
        validated_data['quantity'] = instance.quantity + adjustment
        return super().update(instance, validated_data)
