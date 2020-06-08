"""Farmzone URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see.
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

# from backend.farmzone_users.views import FarmzoneUserViewSet

router = DefaultRouter()
# router.register(r'users', FarmzoneUserViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path("", TemplateView.as_view(template_name="home.html"), name="home"),
                  path('api-auth/', include('rest_framework.urls')),
                  path('login/', views.obtain_auth_token),
                  path('api/', include(router.urls)),
                  # path('market/', include('backend.marketplace.urls')),
                  # path('forum/', include('backend.forum.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),

                  path('', include('farmzoneweb.urls', namespace='farmzoneweb')),

                  path('api/', include('frontend.core.api.urls')),

                  path('auth/', include('frontend.accounts.urls')),
                  path('ads/', include('frontend.ads.urls')),
                  path('users/', include('users.urls')),
                  path('', include('frontend.core.urls')),
                  path('categories', include('frontend.category.urls')),

                  path('', include('frontend.forum.urls')),

                  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
