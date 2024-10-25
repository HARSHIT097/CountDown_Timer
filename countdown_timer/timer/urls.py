# timer/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.countdown_view, name='countdown'),
]
