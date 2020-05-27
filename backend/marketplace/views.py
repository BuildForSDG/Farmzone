"""Views module focuses on API views."""

from rest_framework import viewsets
from .models import ProductsAds, Category, Pricing, Reviews
from .serializers import ProductsAdsSerializers, CategorySerializer, PricingSerializer, ReviewsSerializer


class ProductsAdsView(viewsets.ModelViewSet):
    """Handles the database objects access."""

    queryset = ProductsAds.objects.all()
    serializer_class = ProductsAdsSerializers


class CategoryView(viewsets.ModelViewSet):
    """Category Views."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PricingViews(viewsets.ModelViewSet):
    """Pricing Views."""

    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer


class ReviewsView(viewsets.ModelViewSet):
    """Reviews Views."""

    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
