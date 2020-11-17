from .models import *
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.response import Response
import logging
logger = logging.getLogger(__name__)
# stock_price
class CurrentStockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentStockPrice
        fields = '__all__'

class CurrentStockPriceViewSet(viewsets.ModelViewSet):
    queryset = currentStockPrice.objects.all()
    serializer_class = CurrentStockPriceSerializer

# news_data
class NewsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = newsData
        fields = '__all__'

class NewsDataViewSet(viewsets.ModelViewSet):
    queryset = newsData.objects.all()
    serializer_class = NewsDataSerializer

# current_stock
class CurrentStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentStock
        fields = '__all__'

class CurrentStockViewSet(viewsets.ModelViewSet):
    queryset = currentStock.objects.all()
    serializer_class = CurrentStockSerializer

# user_rank
class UserRankSerializer(serializers.ModelSerializer):
    class Meta:
        model = userRank
        fields = '__all__'

class UserRankViewSet(viewsets.ModelViewSet):
    queryset = userRank.objects.all()
    serializer_class = UserRankSerializer
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        res = Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        print(res.data)
        return res

# trading_log
class TradingLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = tradingLog
        fields = '__all__'

class TradingLogViewSet(viewsets.ModelViewSet):
    queryset = tradingLog.objects.all()
    serializer_class = TradingLogSerializer
