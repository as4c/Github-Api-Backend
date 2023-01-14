from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from .views import UserView

urlpatterns = [
    path('api/user/<str:username>/', UserView.as_view()),
]
