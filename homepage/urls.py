from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('features/', views.features, name='features'),
    path('stats/', views.stats, name='stats'),
    path('contact/', views.contact, name='contact'),
]