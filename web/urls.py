from django.urls import path, include
from . import views

urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('test/', views.test, name='test'),
    path('base/', views.base, name='base'),
]
