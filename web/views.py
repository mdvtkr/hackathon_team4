from django.shortcuts import render
from django.views import View
from django.conf import settings

from django.http import JsonResponse
import urllib.request as req
import urllib.parse as parse
import requests

# Create your views here.
def intro(request):
    return render(request, 'web/intro.html')

def test(request):
    return render(request, 'web/test.html')

def base(request):
    return render(request, 'web/base.html')

def getCurrentStockPrice(request):
    return JsonResponse(koscomApi())


def koscomApi():
    marketCode = 'kospi'
    url = 'https://sandbox-apigw.koscom.co.kr/v2/market/stocks/'+marketCode+'/lists'
    headers = {'apiKey':'l7xxc59a3df427af489fa4234dce296492f3'}
    res = requests.get(url, headers=headers)
    return res.json()