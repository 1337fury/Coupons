from rest_framework import serializers
from .models import Coupon, Subscriber

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = ['id', 'title', 'description', 'code', 'discount_amount', 
                 'valid_from', 'valid_until', 'is_active', 'created_at', 'image', 'category']

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['id', 'email', 'is_active', 'subscribed_at']