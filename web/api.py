from .models import *
from rest_framework import serializers, viewsets

class CurrentStockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = currentStockPrice
        fields = '__all__'

class CurrentStockPriceViewSet(viewsets.ModelViewSet):
    queryset = currentStockPrice.objects.all()
    serializer_class = CurrentStockPriceSerializer
