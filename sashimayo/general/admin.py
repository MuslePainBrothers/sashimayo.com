from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title', {'fields': ['title']}),
        ('description', {'fields': ['description']}),
        ('category', {'fields': ['category']}),
    ]
admin.site.register(Product, ProductAdmin)
