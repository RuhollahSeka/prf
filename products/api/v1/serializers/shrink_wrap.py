from rest_framework import serializers

from products.models import ShrinkWrap


class ShrinkWrapSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShrinkWrap
        fields = (
            'id',
            'name',
        )
