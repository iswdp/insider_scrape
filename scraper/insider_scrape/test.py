import datetime, pickle, time, urllib.parse, urllib.request
from urllib.request import urlopen
from datetime import timedelta
import requests

def make_unix_time_for_today():
    x = datetime.datetime.today()
    y = x.replace(hour=0, minute=0, second=0, microsecond=0)
    unixtime = int(time.mktime(y.timetuple()))
    return unixtime

today_unix = make_unix_time_for_today()
header = {'Connection': 'keep-alive',
            'Expires': '-1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
            }

cookies = {'B': 'cf44em1evvsp6&b=3&s=3n'}

x = datetime.datetime.today()
y = x.replace(hour=0, minute=0, second=0, microsecond=0)
delta = timedelta(days=1)

lookback_ts = y - (delta * 15)
lookback_ts = int(time.mktime(lookback_ts.timetuple()))

url = 'https://query1.finance.yahoo.com/v7/finance/download/' + symbol + '?period1=' + str(lookback_ts) + '&period2=' + str(today_unix) + '&interval=1d&events=history'
page = requests.get(url, headers=header, cookies=cookies)

the_page = page.content