from django.urls import path
from base import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('exeption_view', views.exeption_view, name='exeption_view'),
]