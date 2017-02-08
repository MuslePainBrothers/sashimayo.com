from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        ('title', {'fields': ['title']}),
        ('description', {'fields': ['description']}),
        ('tags', {'fields': ['tags']}),
    ]
admin.site.register(Product, ProductAdmin)
