from django_filters import rest_framework as filters

from frontend.core.models import Ad


class AdFilter(filters.FilterSet):
    class Meta:
        model = Ad
        fields = ['category']
