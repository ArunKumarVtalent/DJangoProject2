from django.urls import path
from . import views

urlpatterns = [
    path('', views.demonew, name='demonew'),
    path('demonew/', views.demonew, name='demonew1'),
]