import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# from mpl_finance import candlestick2_ohlc
import mplfinance as mpf

import numpy as np
import datetime
import os

FILE_TYPE='.png'

def ohlc_to_image(tickers, start=0, end=0, category="daily", dpi=300):
    for ticker in tickers:
        
        path = f'./datasets/{ticker}'
        if not os.path.isdir(path):
            os.mkdir(path)

        try:
            print(f"{ticker} : start -> ", end="")
            
            csv_data = pd.read_csv(f"./datasets/{category}/{ticker}.csv")
            if (not start) and (not end):
                csv_data = csv_data[start:end]
            #종가의 데이터를  가지고 꺽은선 그래프를 만든다.
            plt.plot(csv_data["Close"])
            # plt.ylabel("Close")
            # plt.xlabel("Date")
            # plt.title("apple")
            plt.savefig(f'{path}/{ticker}_line_close.png', dpi=dpi)
            plt.clf()
            '''
            캔들 지금 오류나서 수정중
            https://github.com/matplotlib/mplfinance
            #데이터를 가지고 캔들 그래프를 만든다.
            fig = plt.figure()
            ax = fig.add_subplot(1,1,1)
            candlestick2_ohlc(ax, csv_test['Open'], csv_test['High'], csv_test['Low'], csv_test['Close'], width=0.5,colorup='r', colordown='b')
            #plt.grid()
            plt.savefig(f'{path}/{ticker}_candle.png', dpi=dpi)
            '''
            print("done")

        except err:
            print(err)
            print(f"{ticker} 에서 오류발생")
        

#tickers: ticker의 집합, 
#start, end --> start번쨰 데이터 부터 end번쨰 데이터 까지
#category --> 몇일봉 데이터인지
#dpi --> 사진 저장 화질
tickers = ['AAPL', "MSFT", "C"]
ohlc_to_image(tickers, 0, 30)