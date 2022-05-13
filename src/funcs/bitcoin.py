import urllib.request


def callprice():
    url = "https://api.nomics.com/v1/currencies/ticker?key=dd0cbd0caa3304341d346aae58955bdf7238ec44&ids=BTC,ETH,XRP&interval=1d,30d&convert=EUR&platform-currency=ETH&per-page=100&page=1"
    return urllib.request.urlopen(url).read()


