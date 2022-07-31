from django import views
from django.contrib import admin
from django.urls import path, include

import v1.views as views

urlpatterns = [
    path('', views.home, name='home')
]