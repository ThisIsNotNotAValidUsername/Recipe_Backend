from django.contrib import admin
from django.urls import path, include
from .views import api_test

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/test/", api_test),
    path("api/recipes/", include("recipes.urls")),
]
