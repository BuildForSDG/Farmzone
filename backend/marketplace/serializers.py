"""Serializers module will handle all the object serialization for all the models."""

from rest_framework import serializers

from . import models


# noqa: D212,D204,D404

class ProductsAdsSerializers(serializers.ModelSerializer):
    """
    Serializes and deserializes python objects to JSON data.
    """

    class Meta:

        """Defines models and fields to be serialized."""

        model = models.ProductsAds
        fields = ("ads_id", "pricing_id", "category_id", "user_id",
                  "Ads_content", "activity", "Ads_title")

    def update(self, instance, validated_data):
        """Update method updates the products objects and save then to the DB."""
        self.instance.Ads_content = validated_data.get("Ads_content", self.instance.Ads_content)
        self.instance.activity = validated_data.get("activity", self.instance.activity)
        self.instance.Ads_title = validated_data.get("Ads_title", self.instance.Ads_title)
        self.instance.save()

        return self.instance
