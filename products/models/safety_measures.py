from django.db import models

from common.models import TimedModel
from products.models import Variant, GHSStatement, InternationalRegulation


class SafetyMeasures(TimedModel):
    variant = models.OneToOneField(
        to=Variant,
        on_delete=models.CASCADE,
    )

    # Hazard Identification
    hazard_phrases = models.TextField(
        blank=True,
    )

    precautionary_phrases = models.ManyToManyField(
        to=GHSStatement,
        related_name='safety_measures',
    )

    # First Aid Measures
    inhalation_measures = models.TextField(
        blank=True,
    )

    eye_contact_measures = models.TextField(
        blank=True,
    )

    skin_contact_measures = models.TextField(
        blank=True,
    )

    ingestion = models.TextField(
        blank=True,
    )

    # Fire Fighting Measures
    fire_fighting_measures = models.TextField(
        blank=True,
    )

    # Accidental Release Measures
    individual_precautions = models.TextField(
        blank=True,
    )

    clean_up_procedures = models.TextField(
        blank=True,
    )

    # Handling and Storage
    storage_conditions = models.TextField(
        blank=True,
    )

    handling_procedures = models.TextField(
        blank=True,
    )

    # Exposure Controls
    exposure_limits = models.TextField(
        blank=True,
    )

    # Stability and Reactivity
    period_after_opening = models.TextField(
        blank=True,
    )

    Dangerous_reactions = models.TextField(
        blank=True,
    )

    # Toxicological Information
    toxicological_information = models.TextField(
        blank=True,
    )

    # Ecological Information
    ecological_information = models.TextField(
        blank=True,
    )

    # Disposal Consideration
    disposal_consideration = models.TextField(
        blank=True,
    )

    # Transport Information
    general_transport_information = models.TextField(
        blank=True,
    )

    international_regulations = models.ManyToManyField(
        to=InternationalRegulation,
        related_name='safety_measures',
    )

    transport_class = models.TextField(
        blank=True,
    )

    transport_packing_group = models.TextField(
        blank=True,
    )

    transport_material_code = models.TextField(
        blank=True,
    )

    transport_labelling = models.TextField(
        blank=True,
    )

    # Regulatory Information
    general_regulatory_information = models.TextField(
        blank=True,
    )

    # Other Information
    extra_information = models.TextField(
        blank=True,
    )
