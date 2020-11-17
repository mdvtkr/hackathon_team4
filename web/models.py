from django.db import models

class currentStockPrice(models.Model):
    stock_code = models.CharField(primary_key=True,max_length=30)
    stock_name = models.CharField(max_length=30)
    current_price = models.IntegerField()

# 사전 지정해놓은 뉴스 데이
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

#
class currentStock(models.Model):
    stock_code = models.CharField(primary_key=True,max_length=30)
    stock_name = models.CharField(max_length=30, default="stock_name")
    stock_quantity = models.IntegerField()
    future_price = models.IntegerField()
    current_price = models.IntegerField()
    previous_price = models.IntegerField()

class userRank(models.Model):
    # id = models.AutoField()
    username = models.CharField(max_length=30, primary_key=True)
    deposit = models.IntegerField(default=1000000)
    earning_rate = models.FloatField(default=0)
    # date = models.DateTimeField(auto_now_add=True)

class tradingLog(models.Model):
    id = models.AutoField(primary_key=True)
    round = models.IntegerField()
    stock_code = models.CharField(max_length=30)
    sell_count = models.IntegerField()
    buy_count = models.IntegerField()

class stockReference(models.Model):
    stock_code = models.CharField(primary_key=True,max_length=30)
    stock_name = models.CharField(max_length = 30)

class stockList(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length = 30)
    stock = models.ForeignKey(currentStock, on_delete=models.CASCADE)
# Create your models here.
