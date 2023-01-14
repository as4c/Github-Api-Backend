from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('heroapi.urls'))
]
