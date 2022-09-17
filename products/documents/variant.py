from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from products.models import Variant


@registry.register_document
class VariantDocument(Document):
    components = fields.NestedField(
        properties={
            'name': fields.TextField(),
            'code': fields.TextField(),
        }
    )

    ingredients = fields.NestedField(
        properties={
            'chemical_name': fields.NestedField(),
        }
    )

    safety_measures = fields.ObjectField(
        properties={
            'inhalation_measures': fields.TextField(),
            'eye_contact_measures': fields.TextField(),
            'skin_contact_measures': fields.TextField(),
            'ingestion': fields.TextField(),
            'fire_fighting_measures': fields.TextField(),
            'individual_precautions': fields.TextField(),
            'clean_up_procedures': fields.TextField(),
            'storage_conditions': fields.TextField(),
            'handling_procedures': fields.TextField(),
            'exposure_limits': fields.TextField(),
            'dangerous_reactions': fields.TextField(),
            'toxicological_information': fields.TextField(),
            'ecological_information': fields.TextField(),
            'disposal_consideration': fields.TextField(),
            'general_transport_information': fields.TextField(),
            'transport_class': fields.TextField(),
            'transport_packing_group': fields.TextField(),
            'transport_material_code': fields.TextField(),
            'transport_labelling': fields.TextField(),
            'general_regulatory_information': fields.TextField(),
            'extra_information': fields.TextField(),
        }
    )

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

    def get_queryset(self):
        return super().get_queryset().select_related(
            'safety_measures',
        ).prefetch_related(
            'ingredients', 'components',
        )
