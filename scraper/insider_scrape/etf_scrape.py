#!../../venv/bin/python3

import datetime, pickle, time, urllib.parse, urllib.request
from urllib.request import urlopen
from datetime import timedelta
from etf_symbols import etf_symbols

def make_unix_time_for_today():
    x = datetime.datetime.today()
    y = x.replace(hour=0, minute=0, second=0, microsecond=0)
    unixtime = int(time.mktime(y.timetuple()))
    return unixtime

def import_yahoo_stock_prices(symbol):
    today_unix = make_unix_time_for_today()

    x = datetime.datetime.today()
    y = x.replace(hour=0, minute=0, second=0, microsecond=0)
    delta = timedelta(days=1)

    lookback_ts = y - (delta * 5)
    lookback_ts = int(time.mktime(lookback_ts.timetuple()))

    url = 'https://query1.finance.yahoo.com/v7/finance/download/' + symbol + '?period1=' + str(1325376000) + '&period2=' + str(today_unix) + '&interval=1d&events=history&crumb=ugn9ld9qJFm'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    values = {'name': 'Michael Foord',
              'location': 'Northampton',
              'language': 'Python' }
    headers = {'User-Agent': user_agent}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data, headers)
    with urllib.request.urlopen(req) as response:
       the_page = response.read()
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
        except:
            if j < 9:
                print('---Attempt ' + str(j + 2) + '---')
            else:
                failed_list.append(str(i))
                print('--------------------Failed--------------------')

with open('etf_failed_list.list', 'wb') as fi:
    pickle.dump(failed_list, fi)

print('Historical data retrieved...\n')