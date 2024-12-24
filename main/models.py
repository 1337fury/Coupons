from django.db import models
import os

class Coupon(models.Model):
    CATEGORY_CHOICES = [
        ('GROCERIES', 'Groceries'),
        ('CLOTHING', 'Clothing'),
        ('ELECTRONICS', 'Electronics'),
        ('BOOKS', 'Books'),
        ('HOME_GARDEN', 'Home & Garden'),
        ('FASHION', 'Fashion'),
        ('SPORTS', 'Sports'),
        ('ENTERTAINMENT', 'Entertainment')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    code = models.CharField(max_length=50, unique=True)
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_until = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='coupons/', null=True, blank=True)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='GROCERIES'
    )

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete the image file when the coupon is deleted
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)