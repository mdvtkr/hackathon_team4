"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
import web.api

router = routers.DefaultRouter()
router.register('stock_price',web.api.CurrentStockPriceViewSet)
router.register('current_stock', web.api.CurrentStockViewSet)
router.register('news_data', web.api.NewsDataViewSet)
router.register('user_rank', web.api.UserRankViewSet)
router.register('trading_log', web.api.TradingLogViewSet)

urlpatterns = [
    path('', include('web.urls')),
    path('admin/', admin.site.urls),
    path('api/swagger', get_swagger_view(title='swagger')),
    path('api/v1/', include((router.urls,'web'), namespace='api')),
]
