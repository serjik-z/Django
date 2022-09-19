from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.index1, name='about'),
]

