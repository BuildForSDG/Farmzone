"""Models file handles all the API MODELS."""


from django.db import models

from backend.common.models import AbstractBase


# noqa: D212,D204,D404

class Users(AbstractBase):
    """
    A Class to handle user details in the farm zone App.
    """

    # user_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    full_names = models.CharField(max_length=45, null=False, blank=False)
    user_type = models.BooleanField(null=False, blank=False)
    activity = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=45, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, default='+254700000000')
    email = models.CharField(max_length=45, null=True, blank=True)

    @property
    def user_data(self):
        """User computations function user_data."""
        return '{} {} {} {} {} {} {}'.format(
            self.id or '',
            self.full_names or '',
            self.user_type or '',
            self.activity or '',
            self.location or '',
            self.phone_number or '',
            self.email or ''
        )

    def __str__(self):
        """Printable representation of string objects."""
        return "Reviews: {}".format(self.user_data)


# noqa: D212,D204,D404

class Category(AbstractBase):
    """
    Class Categorizes all the Products in the platform.
    """

    # category_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    category_name = models.CharField(max_length=45, null=False, blank=False, unique=True)
    category_description = models.CharField(max_length=10000, null=False, blank=False)

    @property
    def category_data(self):
        """Category computations function category_data."""
        return '{} {} {}'.format(
            self.id or '',
            self.category_name or '',
            self.category_description or ''
        )

    def __str__(self):
        """Printable representation of string objects."""
        return "Reviews: {}".format(self.category_data)


# noqa: D212,D204,D404

class Pricing(AbstractBase):
    """
    Class to handle various products pricing.
    """

    # pricing_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    value = models.CharField(max_length=45, blank=False, null=False)
    commodity = models.CharField(max_length=45, null=False, blank=False)
    description = models.TextField(editable=False, null=False, blank=False)
    category_id = models.ForeignKey(Category, verbose_name="category", on_delete=models.CASCADE)

    @property
    def pricing_data(self):
        """Pricing computations function pricing_data."""
        return '{} {} {} {}'.format(
            self.id or '',
            self.value or '',
            self.commodity or '',
            self.description or ''
        )

    def __str__(self):
        """Printable representation of string objects."""
        return "Reviews: {}".format(self.pricing_data)


# noqa: D212,D204,D404

class ProductsAds(AbstractBase):
    """
    Get hold of farmers Ads products data.
    """

    # ads_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    pricing_id = models.ForeignKey(Pricing, default=1, verbose_name="pricing",
                                   on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,
                                    default=1,
                                    verbose_name="category",
                                    on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, default=1, verbose_name="users", on_delete=models.CASCADE)
    Ads_content = models.ImageField(upload_to=None, height_field=None, width_field=None,
                                    max_length=256, null=False)
    activity = models.CharField(max_length=256, null=False, blank=False)
    Ads_title = models.CharField(max_length=256, null=False, blank=False)

    @property
    def product_data(self):
        """Ads computations function product_data."""
        return '{} {} {} {}'.format(
            self.id or '',
            self.Ads_content or '',
            self.activity or '',
            self.Ads_title or ''
        )

    def __str__(self):
        """Printable representation of string objects."""
        return "ProductsAds: {}".format(self.product_data)


# noqa: D212,D204,D404, D213

class Reviews(AbstractBase):
    # reviews_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    status = models.BooleanField()
    review_message = models.TextField(editable=False, null=False, blank=False)
    date = models.DateField(auto_now=True)
    user_id = models.ForeignKey(Users, verbose_name="user", on_delete=models.CASCADE)
    ads_id = models.ForeignKey(ProductsAds, verbose_name="ads", on_delete=models.CASCADE)

    @property
    def reviews_data(self):
        """Reviews computations function reviews_data."""
        return '{} {} {} {}'.format(
            self.id or '',
            self.status or '',
            self.review_message or '',
            self.date or ''
        )

    def __str__(self):
        """Printable representation of string objects."""
        return "Reviews: {}".format(self.reviews_data)
