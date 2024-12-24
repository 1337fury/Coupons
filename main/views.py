# main/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from django.shortcuts import get_object_or_404
from .models import Coupon, Subscriber
from .serializers import CouponSerializer, SubscriberSerializer

class CouponViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    def retrieve(self, request, pk=None):
        """
        Get a coupon by its ID.
        """
        try:
            coupon = get_object_or_404(Coupon, pk=pk)
            serializer = self.get_serializer(coupon)
            return Response(serializer.data)
        except:
            return Response(
                {'error': 'Coupon not found'},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(detail=False, methods=['GET'])
    def active(self, request):
        active_coupons = Coupon.objects.filter(
            is_active=True,
            valid_from__lte=timezone.now(),
            valid_until__gte=timezone.now()
        )
        serializer = self.get_serializer(active_coupons, many=True)
        return Response(serializer.data)

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Check if email already exists
            email = serializer.validated_data['email']
            if Subscriber.objects.filter(email=email).exists():
                return Response(
                    {'error': 'Email already subscribed'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
