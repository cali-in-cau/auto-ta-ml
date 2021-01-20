import os
import yfinance as yf
import datetime as dt


def download_ohlc_from_yahoo():
    today = dt.datetime.today().strftime("%Y-%m-%d")
    one_year_ago = (dt.datetime.today() - dt.timedelta(days=365)).strftime("%Y-%m-%d")

    with open("datasets/ticker.csv") as f:
        #in ticker, top 100 stocks in NADAQ        
        print("Download Daily OHLC csv from {0} to {1}".format(one_year_ago, today))
        path = './datasets/daily'
        
        if not os.path.isdir(path):
            os.mkdir(path)
        
        for line in f:
            if "," not in line:
                continue
            symbol = line.split(",")[0]
            data = yf.download(symbol, start=one_year_ago, end=today)
            data.to_csv('datasets/daily/{}.csv'.format(symbol))        


download_ohlc_from_yahoo()
