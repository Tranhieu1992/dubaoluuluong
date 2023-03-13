from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('result', views.result),
    path('model', views.model),
    path('base', views.base)
]