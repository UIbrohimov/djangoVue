from typing import Callable
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
# Create your views here.


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


latest_products_list = LatestProductsList.as_view()


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)


product_detail_view = ProductDetail.as_view()


class GetCategories(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


categories_list = GetCategories.as_view()
