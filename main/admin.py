from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Coupon, Subscriber

# Unregister the default User and Group models
admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
   list_display = ('title', 'code', 'category', 'discount_amount', 'valid_from', 'valid_until', 'is_active')
   list_filter = ('is_active', 'valid_from', 'valid_until', 'category')
   search_fields = ('title', 'code', 'description')

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
   list_display = ('email', 'is_active', 'subscribed_at')
   list_filter = ('is_active',)
   search_fields = ('email',)