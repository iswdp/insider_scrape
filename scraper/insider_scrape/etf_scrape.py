#!/usr/bin/env python3

import datetime, pickle, time, urllib.parse, urllib.request
from urllib.request import urlopen
from datetime import timedelta
from etf_symbols import etf_symbols
import requests

def make_unix_time_for_today():
    x = datetime.datetime.today()
    y = x.replace(hour=0, minute=0, second=0, microsecond=0)
    unixtime = int(time.mktime(y.timetuple()))
    return unixtime

def import_yahoo_stock_prices(symbol):
    session = requests.session()
    session.proxies = {}
    header = {'Connection': 'keep-alive',
                'Expires': '-1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
                }

    today_unix = make_unix_time_for_today()

    x = datetime.datetime.today()
    y = x.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = timedelta(days=1)

    lookback_ts = y - (delta * 7)
    lookback_ts = int(time.mktime(lookback_ts.timetuple()))

    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + symbol + '?period1=' + str(lookback_ts) + '&period2=' + str(today_unix) + '&interval=1d&events=history'
    page = session.get(url, headers=header)

    the_page = page.content
    return the_page

print('---Downloading Historical Data---')

#with open('etf_symbol_list.list', 'rb') as fi:
    #symbols = pickle.load(fi)

symbols = etf_symbols

failed_list = []
counter = 0

for i in symbols:
    print(i + '    ' + str(counter))
    counter += 1

    for j in range(2):
        try:
            temp = import_yahoo_stock_prices(str(i))
            name = 'etf_data/' + i + '.csv'
            with open(str(name), 'wb') as w:
                w.write(temp)
            break
        except Exception as e: 
            print(e)
            if j < 9:
                print('---Attempt ' + str(j + 2) + '---')
            else:
                failed_list.append(str(i))
                print('--------------------Failed--------------------')
    time.sleep(2)

with open('etf_failed_list.list', 'wb') as fi:
    pickle.dump(failed_list, fi)

print('Historical data retrieved...\n')