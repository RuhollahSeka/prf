from rest_framework import serializers

from product_requests.models import Job


class JobEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = (
            'id',
            'product_request',
            'product',
            'quantity',
        )

    def create(self, validated_data):
        validated_data['fulfiller'] = self.context['request'].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['fulfiller'] = self.context['request'].user
        return super().update(instance, validated_data)
