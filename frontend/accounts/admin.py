
from django.contrib import admin

# add user to admin backend
from .models import User
# Register your models here.
admin.site.register(User)