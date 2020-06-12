from django.contrib.postgres.fields import ArrayField
from django.db import models
from backend.common.models import AbstractBase


class Location(AbstractBase):
    # pylint: disable=missing-docstring

    location_name = models.CharField(
        max_length=100, null=True, blank=True)
    estate = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(
        max_length=100, unique=True)
    post_code = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.CharField(
        max_length=10, null=True, blank=True)
    coordinates = ArrayField(
        models.CharField(max_length=10, blank=True), size=2,
        blank=True, default=list)

    def __str__(self):
        """String representation for the class."""
        return "Location: (county={}, country={})".format(
            self.county, self.country)
