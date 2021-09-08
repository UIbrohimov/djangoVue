from django.contrib import admin

from apps.core.models import Picture
from .models import Category, Product

# Register your models here.


class PictureInline(admin.StackedInline):
    model = Picture
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    
    def get_prepopulated_fields(self, request, obj):
        return {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    
    # inlines = [PictureInline]

    def get_prepopulated_fields(self, request, obj):
        return {'slug': ('title',)}
