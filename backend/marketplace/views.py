"""Views module focuses on API views."""

from rest_framework import viewsets
from .models import ProductsAds, Category, Pricing, Reviews
from .serializers import ProductsAdsSerializers, CategorySerializer, PricingSerializer, ReviewsSerializer


class ProductsAdsView(viewsets.ModelViewSet):
    """Handles the database objects access."""

    queryset = ProductsAds.objects.all()
    serializer_class = ProductsAdsSerializers


class CategoryView(viewsets.ModelViewSet):
    """Handle category views."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PricingViews(viewsets.ModelViewSet):
    """Handle pricing views."""

    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class ReviewsView(viewsets.ModelViewSet):
    """Handle review views."""

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
