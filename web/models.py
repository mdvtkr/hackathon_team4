from django.db import models

class currentStockPrice(models.Model):
    stock_code = models.IntegerField(primary_key=True)
    stock_name = models.CharField(max_length=30)
    current_price = models.IntegerField()

class newsData(models.Model):
    id = models.AutoField(primary_key=True)
    news_data = models.CharField(max_length=300)
    stock_name = models.CharField(max_length=30)
    current_price = models.IntegerField()
    rate_005930 = models.IntegerField()
    rate_000660 = models.IntegerField()
    rate_068270 = models.IntegerField()
    rate_096530 = models.IntegerField()
    rate_105560 = models.IntegerField()
    rate_055550 = models.IntegerField()
    rate_009540 = models.IntegerField()
    rate_133750 = models.IntegerField()
    rate_057030 = models.IntegerField()
    rate_035720 = models.IntegerField()
    rate_035420 = models.IntegerField()
    rate_035760 = models.IntegerField()
    rate_352820 = models.IntegerField()
    rate_009830 = models.IntegerField()
    rate_011780 = models.IntegerField()
    rate_011070 = models.IntegerField()

class currentStock(models.Model):
    stock_code = models.IntegerField(primary_key=True)
    stock_quantity = models.IntegerField()
    average_price = models.IntegerField()
    current_price = models.IntegerField()
    earning_rate = models.IntegerField()

class userRank(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 30)
    earning_rate = models.IntegerField()
    # date = models.DateTimeField(auto_now_add=True)

class tradingLog(models.Model):
    id = models.AutoField(primary_key=True)
    round = models.IntegerField()
    stock_code = models.IntegerField()
    sell_count = models.IntegerField()
    buy_count = models.IntegerField()

class stockReference(models.Model):
    stock_code = models.IntegerField(primary_key=True)
    stock_name = models.CharField(max_length = 30)

# Create your models here.
