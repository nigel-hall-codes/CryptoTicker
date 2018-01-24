import time
import urllib2
import json
import datetime


def getPCtCh(yday, now):
    return now/yday-1

def gethistoricalPrice(crypto):
    today = datetime.datetime.today()
    date = today - datetime.timedelta(days=1)
    ts = str(time.mktime(date.timetuple()))
    url = 'https://min-api.cryptocompare.com/data/pricehistorical?fsym={}&tsyms=USD&ts={}&extraParams=your_app_name'.format(crypto, ts)
    data = urllib2.urlopen(url).read()
    # print data
    return json.loads(data)[crypto]['USD']


# cryptos = ['BTC', 'XRP', 'ETH', 'LTC']

def getTickerData(cryptos):

    tickerData = {}
    tickerString = ""

    for c in cryptos:
        url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms=USD'.format(c)
        data = urllib2.urlopen(url).read()
        data = json.loads(data)
        # print data
        price = data['USD']
        yday = gethistoricalPrice(c)
        pct_ch = "%.2f" % ((price/ yday -1) * 100) + '%'

        tickerData[c] = {'price': price, 'pct_ch': pct_ch}
        # tickerString += c + " " + str(price) + " " + str(pct_ch) + ' '

    return tickerData




# print gethistoricalPrice('BTC')

# print getTickerData(cryptos)



