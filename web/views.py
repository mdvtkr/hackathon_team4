from django.shortcuts import render
from django.views import View
from django.conf import settings
from django.http import JsonResponse
from .api import *
from .models import *
from rest_framework import status
from rest_framework.decorators import renderer_classes, api_view
from rest_framework_swagger import renderers
from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404


import requests
import datetime
import logging
from .batch import *

logger = logging.getLogger(__name__)
# Create your views here.
def intro(request):
    if request.method == "GET":
        logger.debug("logger.debug", request.GET)
        logger.info("logger.info", request.POST)
        logger.debug('request POST AJAX')
        print("request POST AJAX")
        print(request.POST)
    return render(request, 'web/intro.html')



def test(request):
    return render(request, 'web/test.html')

def base(request):
    if request.method == "POST":
        logger.debug(request.POST)
        logger.info(request.POST)
        logger.debug('request POST AJAX')
        print("request POST AJAX")
        print(request.POST)
    return render(request, 'web/base.html')

def ranking(request):
    return render(request, 'web/ranking.html')

def baseNext(request, pk):
    user = get_object_or_404(userRank, pk=pk)
    return render(request, 'web/base.html')




# API
@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def stockList(request):
    return JsonResponse(koscomStockList(), safe=False)
@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def stockPriceList(request):
    return JsonResponse(koscomStockPriceList(), safe=False)
@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def currentStockRefresh(request):
    return JsonResponse(currentStockBatch(), safe=False)
@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def tradingLogClear(request):
    return JsonResponse(tradingLogClearDB(),safe=False)
@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def currentStockClear(request):
    return JsonResponse(currentStockClearDB(),safe=False)
@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def userClear(request):
    return JsonResponse(userRankClearDB(),safe=False)


# Server Logic
def tradingLogClearDB():
    return tradingLog.objects.all().delete()
def currentStockClearDB():
    return currentStock.objects.all().delete()
def userRankClearDB():
    return userRank.objects.all().delete()

# Koscom API
def koscomStockList():
    codes = ['kospi','kosdaq']
    ret = []
    for marketCode in codes:
        url = 'https://sandbox-apigw.koscom.co.kr/v2/market/stocks/'+marketCode+'/lists'
        headers = {'apiKey':'l7xxc59a3df427af489fa4234dce296492f3'}
        res = requests.get(url, headers=headers)
        ret.extend(res.json().get('isuLists'))
    return ret

def koscomStockPriceList():
    url = 'https://sandbox-apigw.koscom.co.kr/v2/market/stocks/'
    now = datetime.datetime.now()
    STOCK_CODE_LIST = ['005930', '000660', '068270', '096530', '105560', '055550', '009540', '133750', '057030',
                       '035720', '035420', '035760', '352820', '009830', '011780', '011070']
    marketCode = 'kospi'
    trnsmCycleTpCd	= 'D'
    inqStrtDd = (now - datetime.timedelta(days=3)).strftime('%Y%m%d')
    inqEndDd = now.strftime('%Y%m%d')
    reqCnt = '3'
    headers = {'apiKey':'l7xxc59a3df427af489fa4234dce296492f3'}

    ret = []

    for stockCode in STOCK_CODE_LIST:
        url = 'https://sandbox-apigw.koscom.co.kr/v2/market/stocks/'+marketCode+'/'+stockCode+'/history?trnsmCycleTpCd='+trnsmCycleTpCd+'&inqStrtDd='+inqStrtDd+'&inqEndDd='+inqEndDd+'&reqCnt='+reqCnt
        res = requests.get(url, headers=headers)
        ret.append(res.json())
    return ret