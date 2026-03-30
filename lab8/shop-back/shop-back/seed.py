"""
Run this once after migrations to add sample data:
    python seed.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from api.models import Category, Product

# Clear existing data
Product.objects.all().delete()
Category.objects.all().delete()

# Create categories
electronics = Category.objects.create(name='Electronics')
clothing = Category.objects.create(name='Clothing')
books = Category.objects.create(name='Books')

# Create products
Product.objects.create(
    name='Wireless Headphones',
    price=49.99,
    description='High-quality noise cancelling headphones.',
    count=50,
    is_active=True,
    category=electronics
)
Product.objects.create(
    name='Mechanical Keyboard',
    price=89.99,
    description='RGB mechanical keyboard with blue switches.',
    count=30,
    is_active=True,
    category=electronics
)
Product.objects.create(
    name='Cotton T-Shirt',
    price=14.99,
    description='100% organic cotton, available in 5 colors.',
    count=200,
    is_active=True,
    category=clothing
)
Product.objects.create(
    name='Winter Jacket',
    price=79.99,
    description='Waterproof jacket for cold weather.',
    count=0,
    is_active=False,
    category=clothing
)
Product.objects.create(
    name='Clean Code',
    price=34.99,
    description='A handbook of agile software craftsmanship by Robert C. Martin.',
    count=15,
    is_active=True,
    category=books
)

print("Seed data created successfully!")
print(f"  Categories: {Category.objects.count()}")
print(f"  Products:   {Product.objects.count()}")
