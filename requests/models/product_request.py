from django.db import models

from common.models import TimedModel
from customers.models import Customer, CustomerAddress
from products.models import PalletType, ShrinkWrap
from users.models import User


class ProductRequest(TimedModel):
    STATUS_DRAFT = 'draft'
    STATUS_PENDING = 'pending'
    STATUS_REJECTED = 'rejected'
    STATUS_CANCELLED = 'cancelled'
    STATUS_CHOICES = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PENDING, 'Pending'),
        (STATUS_REJECTED, 'Rejected'),
        (STATUS_CANCELLED, 'cancelled'),
    )

    requester = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='created_requests',
    )

    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE,
        related_name='product_requests',
    )

    address = models.ForeignKey(
        to=CustomerAddress,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_requests',
    )

    needs_address_label = models.BooleanField()

    status = models.CharField(
        max_length=32,
        choices=STATUS_CHOICES,
    )

    earliest_expected_date = models.DateField()

    pallet_type = models.ForeignKey(
        to=PalletType,
        on_delete=models.CASCADE,
        related_name='product_requests',
    )

    shrink_wrap = models.ForeignKey(
        to=ShrinkWrap,
        on_delete=models.CASCADE,
        related_name='product_requests',
    )

    special_instructions = models.TextField(
        blank=True,
    )
