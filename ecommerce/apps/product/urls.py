from django.urls import path

from .views import latest_products_list, product_detail_view, categories_list

urlpatterns = [
    path('latest-products/', latest_products_list),
    path('categories/', categories_list),
    path('products/<slug:category_slug>/<slug:product_slug>/', product_detail_view),
]
