import random, os
import yfinance as yf
import datetime as dt

from nasdaq_sector import sectors
SAMPLE_NUM = 100

sector_reduced = {}

def random_select_sectors():
    keys = sectors.keys()
    '''
    {'Technology': 651, 'Consumer Cyclical': 498, 'Communication Services': 267, 
    'Financial Services': 1753, 'Healthcare': 1098, 'Consumer Defensive': 215, 'Energy': 284, 
    'Basic Materials': 242, 'Utilities': 106, 'Industrials': 588, 'Real Estate': 299, '': 86, 'Financial': 1, 'Services': 1}
    '''
    for key in keys:
        if(len(sectors[key]) < SAMPLE_NUM):
            continue
        random_sectors = random.sample(sectors[key], SAMPLE_NUM)
        sector_reduced[key] = random_sectors

        path = f'./datasets/{key}'
        if not os.path.isdir(path):
            os.mkdir(path)

def download_ohlc_from_yahoo_sector():
    today = dt.datetime(2021,2,1)
    start = (today - dt.timedelta(days=365 * 5)).strftime("%Y-%m-%d")
    
    keys = sector_reduced.keys()
    for key in keys:
        tickers = sector_reduced[key]
        for ticker in tickers:
            try:
                data = yf.download(ticker, start=start, end=today)
                data.to_csv('datasets/{0}/{1}.csv'.format(key,ticker))
            except:
                #주식 데이터가 전부 없는 경우
                continue


random_select_sectors()
download_ohlc_from_yahoo_sector()