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
from random import randint


import requests
import datetime
import logging
from .batch import *

logger = logging.getLogger(__name__)
# Create your views here.
API_URL = "http://15.164.171.146:8080/api/v1/"
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
# @api_view(['GET'])
# @renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
# def currentStockRefresh(request):
#     return JsonResponse(currentStockBatch(), safe=False)
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
@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def currentStockRefresh(request):
    return JsonResponse(refreshCurrentStock(),safe=False)
@api_view(['GET','POST'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def currentStockAggregate(request):
    return JsonResponse(aggregateCurrentStock(request),safe=False)
@api_view(['GET'])
@renderer_classes([renderers.OpenAPIRenderer, renderers.SwaggerUIRenderer])
def updateCurrentStockAPI(request):
    return JsonResponse(updateCurrentStock(),safe=False)


# Server Logic
def tradingLogClearDB():
    return tradingLog.objects.all().delete()
def currentStockClearDB():
    return currentStock.objects.all().delete()
def userRankClearDB():
    return userRank.objects.all().delete()
def refreshCurrentStock():
    dbUrl = API_URL+'stock_price'
    userUrl = API_URL+'current_stock'
    res1 = requests.get(dbUrl)
    res2 = requests.get(userUrl)
    ret = []
    for stock_user in res2.json():
        for stock_db in res1.json():
            if stock_db.get('stock_code') == stock_user.get('stock_code'):
                stock_user['stock_quantity'] = 0
                stock_user['current_price'] = stock_db['current_price']
                stock_user['previous_price'] = stock_db['current_price']
                stock_user['future_price'] = stock_db['current_price']
                res = requests.put(userUrl+'/'+stock_user['stock_code']+'/',data = stock_user)
                # ret.extend(res.json())
                break
    ret = updateCurrentStock()
    return ret

def aggregateCurrentStock(request):
    print(request.data)
    data = request.data
    url = API_URL+'current_stock'
    userUrl = API_URL + 'user_rank/'+data['username']
    print(userUrl)
    res = requests.get(url)
    sum = 0
    for stock in res.json():
        sum += stock['current_price'] * stock['stock_quantity']
    userRes = requests.get(userUrl)
    curUser = userRes.json()
    deposit = curUser['deposit']
    profit = sum + deposit - 1000000
    profitRatio = (profit / 1000000)*100
    curUser['earning_rate'] = profitRatio
    putUrl = userUrl+'/'
    res2 = requests.put(userUrl, data=curUser)
    return {"profit":profit, "profitRatio":profitRatio}

def updateCurrentStock():
    stockUrl = API_URL+'current_stock'
    newsUrl = API_URL+'news_data'
    stockRes = requests.get(stockUrl).json()
    newsRes = requests.get(newsUrl).json()
    idx = randint(0,len(newsRes)-1)
    news = newsRes[idx]

    for stock in stockRes:
        key = 'rate_'+stock['stock_code']
        cur = stock['current_price']
        stock['current_price'] = stock['future_price']
        stock['previous_price'] = cur
        stock['future_price'] = int(cur*(100+news[key])/100)
        res = requests.put(stockUrl + '/' + stock['stock_code'] + '/', data=stock)
    ret = {}
    ret['news_data'] = news['news_data']
    ret['stock_data'] = stockRes
    return ret

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

#
def getRankingScoreBoard():
    url = API_URL+'user_rank'
    res = requests.get(url)

    res.json