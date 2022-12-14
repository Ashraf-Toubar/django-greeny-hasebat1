from django.contrib import admin

# Register your models here.
from .models import Product, ProductImages, Category, Brand, ProductReview


class ProductImageTabular(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageTabular]
    list_display = ['name', 'flag', 'quantity', 'price']
    list_filter = ['flag', 'brand', 'category', 'price']
    search_fields = ['name', 'desc', 'subtitle']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages)
admin.site.register(ProductReview)
admin.site.register(Brand)
admin.site.register(Category)
