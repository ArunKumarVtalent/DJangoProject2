from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('demo/', views.demo, name='demo1'),
    path('dm/', views.demo, name='demo2'),
    path('Index/', views.demo, name='Index')
]