from django.urls import path, include
from . import views


urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('test/', views.test, name='test'),
    path('base/', views.base, name='base'),
    path('api/stock_list', views.getStockList, name='api'),
    path('api/stock_price', views.getStockPrice, name='api'),
]
