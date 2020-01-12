from django.contrib import admin
from django.urls import path, include

from negosy.apps.landing.views import HomeView

urlpatterns = [
    path('', HomeView.as_view())
]
