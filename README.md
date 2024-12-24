# Coupon API

A simple Django REST API for managing coupons and subscribers.

## Features

- Coupon management with categories
- Public coupon listing and details
- Email subscription system
- Image upload support for coupons

## Quick Start # Coupons

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run migrations

```bash
 python manage.py migrate
```

## Create superuser

```bash
 python manage.py createsuperuser
```

## Run server

```bash
 python manage.py runserver
```

## API Endpoints

- `GET /api/coupons/` - List all coupons
- `GET /api/coupons/<id>/` - Get coupon details
- `GET /api/coupons/active/` - List active coupons
- `POST /api/subscribers/` - Subscribe email