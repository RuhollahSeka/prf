from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from products.models import Variant


@registry.register_document
class VariantDocument(Document):
    class Index:
        name = 'variants'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Variant
        fields = [
            'name',
            'code',
            'description',
            'barcode',
            'carton_barcode',
            'additional_information',
        ]
