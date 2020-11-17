from django.urls import path, include
from . import views

from rest_framework_swagger.views import get_swagger_view

urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('test/', views.test, name='test'),
    path('base/', views.base, name='base'),
    path('ranking/', views.ranking, name='ranking'),
    path('base/<int:pk>/', views.baseNext, name='next'),
    path('api/v1/kospi_stock_list', views.stockList, name='kospi_stock_list'),
    path('api/v1/kospi_stock_price', views.stockPriceList, name='kospi_stock_price'),
    path('api/v1/current_stock_refresh', views.currentStockRefresh, name='current_stock_refresh'),
    path('api/v1/trading_log_clear', views.tradingLogClear, name='trading_log_clear'),
    path('api/v1/current_stock_clear', views.currentStockClear, name='current_stock_clear'),
    path('api/v1/user_clear', views.userClear, name='user_rank_clear'),
    path('api/v1/aggregate', views.currentStockAggregate, name='aggregate'),
    path('api/v1/current_stock_update', views.updateCurrentStockAPI, name='update'),
    path('api/v1/current_stock_batch', views.updateCurrentStockBatch, name='batch'),

    # path('api/current_stock',views.currentStock, name='api'),
]
