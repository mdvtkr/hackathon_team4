import requests

STOCK_CODE_LIST = ['005930','000660','068270','096530','105560','055550','009540','133750','057030','035720','035420','035760','352820','009830','011780','011070']


getUrl = "http://localhost:8000/api/stock_price"
postUrl = 'http://localhost:8000/api/v1/web/'

if __name__ == "__main__":
    res = requests.get(getUrl)
    stockList = res.json()

    for stock in stockList:
        cur = stock.get('result')
        price = cur.get('hisLists')[0].get('opnprc')
        stockCode = cur.get('isuSrtCd')

    # for code in STOCK_CODE_LIST:
    #     res = requests.get(getUrl+code)
    #     cur = res
    #
    #     print(cur)


