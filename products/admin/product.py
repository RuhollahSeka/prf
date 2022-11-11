from django.contrib import admin

from products.models import Product, Variant


class VariantInlineAdmin(admin.StackedInline):
    model = Variant
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
