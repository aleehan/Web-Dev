import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Product, Category


def add_cors_headers(response):
    response['Access-Control-Allow-Origin'] = 'http://localhost:4200'
    response['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
    response['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


# ─── Products ────────────────────────────────────────────────────────────────

def products_list(request):
    #GET /api/products/ — return all products as JSON."""
    products = Product.objects.select_related('category').all()
    data = [p.to_dict() for p in products]
    return add_cors_headers(JsonResponse(data, safe=False))


def product_detail(request, id):
    #GET /api/products/<id>/ — return one product by ID.
    try:
        product = Product.objects.select_related('category').get(pk=id)
        return add_cors_headers(JsonResponse(product.to_dict()))
    except Product.DoesNotExist:
        return add_cors_headers(JsonResponse({'error': 'Product not found'}, status=404))


# ─── Categories ──────────────────────────────────────────────────────────────

def categories_list(request):
    #GET /api/categories/ — return all categories as JSON.
    categories = Category.objects.all()
    data = [c.to_dict() for c in categories]
    return add_cors_headers(JsonResponse(data, safe=False))


def category_detail(request, id):
    #GET /api/categories/<id>/ — return one category by ID.
    try:
        category = Category.objects.get(pk=id)
        return add_cors_headers(JsonResponse(category.to_dict()))
    except Category.DoesNotExist:
        return add_cors_headers(JsonResponse({'error': 'Category not found'}, status=404))


def category_products(request, id):
    #GET /api/categories/<id>/products/ — return all products in a category.
    try:
        category = Category.objects.get(pk=id)
        products = category.products.select_related('category').all()
        data = [p.to_dict() for p in products]
        return add_cors_headers(JsonResponse(data, safe=False))
    except Category.DoesNotExist:
        return add_cors_headers(JsonResponse({'error': 'Category not found'}, status=404))
