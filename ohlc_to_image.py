import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import mplfinance as mpf
#from mpl_finance import candlestick2_ohlc
import numpy as np
import datetime
import os

FILE_TYPE='.png'

def ohlc_to_image(tickers, start=0, end=0, category="daily", dpi=300, type="candle"):
    for ticker in tickers:
        
        path = f'./datasets/{ticker}/'
        if not os.path.isdir(path):
            os.mkdir(path)

        try:
            print(f"{ticker} : start -> ", end="")
            
            csv_data = pd.read_csv(f"./datasets/{category}/{ticker}.csv", index_col=0,parse_dates=True)
            if (start != 0) or (end != 0):
                csv_data = csv_data[start:end]
            csv_data.index.name = "Date"

            mc = mpf.make_marketcolors(up='r',down='b')
            #up과 down에는 색상 지정할수 있다. 예 #ffffff
            s  = mpf.make_mpf_style(marketcolors=mc)
            file_path = path + f'{ticker}_{type}'
    
            savefig = dict(fname=file_path,dpi=300,pad_inches=0.25)
            mpf.plot(csv_data,type=type, style=s, savefig=savefig)

        except err:
            print(err)
            print(f"{ticker} 에서 오류발생")
        
'''
tickers: ticker의 집합, 
start, end --> start번쨰 데이터 부터 end번쨰 데이터 까지 : 전체 날짜 중에서 구간을 선택한다.
category --> 몇일봉 데이터인지
dpi --> 사진 저장 화질
type은 candle 또는 line등등
https://github.com/matplotlib/mplfinance 참고
'''
tickers = ['AAPL', "MSFT", "C"]
ohlc_to_image(tickers, 0, 30, type="candle")
