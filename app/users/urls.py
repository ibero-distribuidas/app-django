from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='users'),
    path('lados/', views.la_dos, name='la_dos'),
]