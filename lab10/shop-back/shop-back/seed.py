
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_back.settings')
django.setup()

from api.models import Category, Product

Product.objects.all().delete()
Category.objects.all().delete()

electronics  = Category.objects.create(name='Electronics')
clothing     = Category.objects.create(name='Clothing')
books        = Category.objects.create(name='Books')
sports       = Category.objects.create(name='Sports')

products = [
    # Electronics (6)
    dict(name='Wireless Headphones',  price=49.99,  description='Noise-cancelling over-ear headphones.',  count=50,  is_active=True,  category=electronics),
    dict(name='Mechanical Keyboard',  price=89.99,  description='RGB keyboard with blue switches.',        count=30,  is_active=True,  category=electronics),
    dict(name='USB-C Hub',            price=29.99,  description='7-in-1 hub with HDMI and PD charging.',  count=100, is_active=True,  category=electronics),
    dict(name='Webcam 1080p',         price=59.99,  description='Full HD webcam with built-in mic.',      count=40,  is_active=True,  category=electronics),
    dict(name='Smart Watch',          price=199.99, description='Fitness tracker with heart rate monitor.',count=20,  is_active=True,  category=electronics),
    dict(name='Portable SSD 1TB',     price=109.99, description='NVMe portable drive, 1000 MB/s.',        count=0,   is_active=False, category=electronics),
    # Clothing (5)
    dict(name='Cotton T-Shirt',       price=14.99,  description='100% organic cotton, 5 colours.',        count=200, is_active=True,  category=clothing),
    dict(name='Winter Jacket',        price=79.99,  description='Waterproof jacket, -20°C rated.',        count=0,   is_active=False, category=clothing),
    dict(name='Running Shorts',       price=24.99,  description='Lightweight moisture-wicking shorts.',   count=80,  is_active=True,  category=clothing),
    dict(name='Wool Beanie',          price=12.99,  description='Warm merino wool beanie, one size.',     count=150, is_active=True,  category=clothing),
    dict(name='Denim Jeans',          price=49.99,  description='Slim fit, stretch denim.',               count=60,  is_active=True,  category=clothing),
    # Books (5)
    dict(name='Clean Code',           price=34.99,  description='Agile software craftsmanship — Robert C. Martin.', count=15, is_active=True, category=books),
    dict(name='The Pragmatic Programmer', price=39.99, description='Your journey to mastery.',            count=10,  is_active=True,  category=books),
    dict(name='Design Patterns',      price=44.99,  description='Gang of Four — reusable OO design.',     count=8,   is_active=True,  category=books),
    dict(name='Python Crash Course',  price=29.99,  description='Hands-on introduction to Python.',       count=25,  is_active=True,  category=books),
    dict(name='You Don\'t Know JS',   price=19.99,  description='Deep dive into JavaScript.',             count=0,   is_active=False, category=books),
    # Sports (4)
    dict(name='Yoga Mat',             price=22.99,  description='Non-slip 6mm TPE mat.',                  count=70,  is_active=True,  category=sports),
    dict(name='Resistance Bands Set', price=17.99,  description='5 resistance levels, latex-free.',       count=90,  is_active=True,  category=sports),
    dict(name='Jump Rope',            price=9.99,   description='Speed rope with ball bearings.',          count=120, is_active=True,  category=sports),
    dict(name='Foam Roller',          price=27.99,  description='High-density muscle recovery roller.',   count=45,  is_active=True,  category=sports),
]

for p in products:
    Product.objects.create(**p)

print(f"Done! Created {Category.objects.count()} categories and {Product.objects.count()} products.")
