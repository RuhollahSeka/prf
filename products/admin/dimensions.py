from django.contrib import admin

from products.models import Dimensions


@admin.register(Dimensions)
class DimensionsAdmin(admin.ModelAdmin):
    pass
