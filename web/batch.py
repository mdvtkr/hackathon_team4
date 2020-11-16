import requests
import json

STOCK_CODE_LIST = ['005930','000660','068270','096530','105560','055550','009540','133750','057030','035720','035420','035760','352820','009830','011780','011070']


getPriceUrl = 'http://13.124.3.123:8080/api/v1/kospi_stock_price'
getListUrl = 'http://13.124.3.123:8080/api/v1/kospi_stock_list'
postUrl = 'http://13.124.3.123:8080/api/v1/stock_price/'

# if __name__ == "__main__":
def currentStockBatch():
    resPrice = requests.get(getPriceUrl)
    resList = requests.get(getListUrl)
    stockPriceList = resPrice.json()#.decode('utf-8')
    stockList = resList.json()
    ret = []
    for stock in stockList:
        if stock.get('isuSrtCd') in STOCK_CODE_LIST:
            cur={}
            cur['stock_code'] = stock.get('isuSrtCd')
            cur['stock_name'] = stock.get('isuKorNm')
            ret.append(cur)
    ret2=[]
    for stock in stockPriceList:
        cur = stock.get('result')
        stockPrice = cur.get('hisLists')[0].get('opnprc')
        stockCode = cur.get('isuSrtCd')
        for n in ret:
            if n.get('stock_code') == stockCode:
                stockName = n.get('stock_name')
                break;
        data = {'stock_code': stockCode, 'current_price': stockPrice, 'stock_name': stockName}
        headers = {'Content-Type': 'application/json'}
        res = requests.put(url=postUrl+data['stock_code']+'/', data=json.dumps(data), headers=headers)
        ret2.append(res.json())
    return ret2
