from django.shortcuts import render
from django.views import View
from django.conf import settings

from django.http import JsonResponse
import urllib.request as req
import urllib.parse as parse
import requests
import datetime

# Create your views here.
def intro(request):
    return render(request, 'web/intro.html')

def test(request):
    return render(request, 'web/test.html')

def base(request):
    return render(request, 'web/base.html')


# API
def getStockList(request):
    return JsonResponse(stockList())

def getStockPrice(request):
    return JsonResponse(stockPriceList(), safe=False)


def stockList():
    marketCode = 'kospi'
    url = 'https://sandbox-apigw.koscom.co.kr/v2/market/stocks/'+marketCode+'/lists'
    headers = {'apiKey':'l7xxc59a3df427af489fa4234dce296492f3'}
    res = requests.get(url, headers=headers)
    return res.json()

def stockPriceList():
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