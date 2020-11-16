from django.urls import path, include
from . import views

from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('test/', views.test, name='test'),
    path('base/', views.base, name='base'),
    path('api/stock_list', views.stockList, name='api'),
    # path('api/stock_price', views.stockPrice, name='api'),
    # path('api/current_stock',views.currentStock, name='api'),
]
