# shop-back — Django REST API

## Setup

```bash
# 1. Create and activate virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run migrations (creates the database tables)
python manage.py makemigrations
python manage.py migrate

# 4. Add sample data (optional but useful for testing)
python seed.py

# 5. Start the server
python manage.py runserver
```

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | /api/products/ | All products |
| GET | /api/products/\<id\>/ | Single product |
| GET | /api/categories/ | All categories |
| GET | /api/categories/\<id\>/ | Single category |
| GET | /api/categories/\<id\>/products/ | Products in a category |

## Connecting to Angular

In your Angular service, set the base URL to:
```
http://localhost:8000
```

Example Angular service call:
```typescript
this.http.get('http://localhost:8000/api/products/')
```
