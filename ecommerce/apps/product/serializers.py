from django.db.models import fields
from rest_framework import serializers

from .models import Category, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'category',
            'description',
            'specs',
            'price',
            'price_discount',
            'id_number',
            'rating',
            'available',
            'bestseller',
            'discount',
            'get_large_image',
            'get_small_image',
            'get_vue_url'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'get_vue_url'
        )

