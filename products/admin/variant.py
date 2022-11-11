from django.contrib import admin

from products.models import Variant


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass
