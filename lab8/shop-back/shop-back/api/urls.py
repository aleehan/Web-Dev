from django.urls import path
from . import views

urlpatterns = [
    # Products
    path('products/', views.products_list),               # /api/products/
    path('products/<int:id>/', views.product_detail),     # /api/products/1/

    # Categories
    path('categories/', views.categories_list),           # /api/categories/
    path('categories/<int:id>/', views.category_detail),  # /api/categories/1/
    path('categories/<int:id>/products/', views.category_products),  # /api/categories/1/products/
]
