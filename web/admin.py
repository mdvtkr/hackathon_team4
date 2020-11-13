from django.contrib import admin
from . import models

@admin.register(models.currentStockPrice)
class CurrentStockPrice(admin.ModelAdmin):
    list_display = (
        'stock_code',
        'stock_name',
        'current_price'
    )

@admin.register(models.newsData)
class NewsData(admin.ModelAdmin):
    list_display = (
        'id',
        'news_data',
        'stock_name',
        'current_price',
        'rate_005930',
        'rate_000660',
        'rate_068270',
        'rate_096530',
        'rate_105560',
        'rate_055550',
        'rate_009540',
        'rate_133750',
        'rate_057030',
        'rate_035720',
        'rate_035420',
        'rate_035760',
        'rate_352820',
        'rate_009830',
        'rate_011780',
        'rate_011070'
    )


@admin.register(models.currentStock)
class CurrentStock(admin.ModelAdmin):
    list_display = (
        'stock_code',
        'stock_quantity',
        'average_price',
        'current_price',
        'earning_rate'
    )

@admin.register(models.userRank)
class UserRank(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'earning_rate'
    )

@admin.register(models.tradingLog)
class TradingLog(admin.ModelAdmin):
    list_display = (
        'id',
        'round',
        'stock_code',
        'sell_count',
        'buy_count'
    )

@admin.register(models.stockReference)
class StockReference(admin.ModelAdmin):
    list_display = (
        'stock_code',
        'stock_name'
    )

# Register your models here.
