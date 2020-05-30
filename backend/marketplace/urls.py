"""Urls file handles  the API urls."""

from django.urls import path, include

from rest_framework import routers

from .views import ProductsAdsView, PricingViews, CategoryView, ReviewsView

router = routers.DefaultRouter()
router.register('ads', ProductsAdsView)
router.register('category', CategoryView)
router.register('pricing', PricingViews)
router.register('reviews', ReviewsView)


urlpatterns = [
    path('', include(router.urls))

]
