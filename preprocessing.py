#!/usr/bin/env python3

import pandas as pd
# from mpl_finance import candlestick2_ohlc
import mplfinance as mpf
import os
import talib
from datetime import datetime
import multiprocessing
from multiprocessing import Pool
from functools import partial
import time

def csv_to_func(ticker, dataset_name):

    try:
        #base_path = f'./pattern_datasets/{dataset_name}'
        base_path = f'./pattern_datasets/{dataset_name}/Industrials'
        if not os.path.isdir(base_path):
            os.makedirs(base_path, exist_ok=True)

        patterns_names = talib.get_function_groups()['Pattern Recognition']
        #print(patterns_names)
        #csv_data = pd.read_csv(f"./datasets/daily/{ticker}",index_col=0,parse_dates=True)
        csv_data = pd.read_csv(f"./datasets/Industrials/{ticker}",index_col=0,parse_dates=True)
        cnt = 1

        for pattern in patterns_names:
            csv_data[pattern] = getattr(talib, pattern)(csv_data['Open'], csv_data['High'], csv_data['Low'], csv_data['Close'])
            tmp_data = csv_data
        
        #해당 구간에서 한번도 패턴이 안나온 항목들을 제외한다.
        zero_column = list(csv_data.columns[(csv_data == 0).all()])
        not_zero_colum = list(set(patterns_names) - set(zero_column))
        
        for pattern in not_zero_colum:
            #print(pattern)
            csv_data_bull = tmp_data[tmp_data[pattern] > 0]
            csv_data_bear = tmp_data[tmp_data[pattern] < 0]
            #각 csv_data에서 양수 인거(보통 100)은 bullish를 나타내고 음수 인거(보통 -100)은 bearish를 나타낸다.
            # 각 패턴이 bull version도 있고 bear 버전도 있다. 따라서 나눠야 한다.
            date_bull = list(map(lambda x : x.strftime("%Y-%m-%d"), csv_data_bull.index))
            date_bear = list(map(lambda x : x.strftime("%Y-%m-%d"), csv_data_bear.index))
            
            for idx, item in enumerate(date_bull):
                make_chart(ticker, tmp_data, item, cnt, pattern, "bull", base_path)
                cnt+=1
            for idx, item in enumerate(date_bear):
                make_chart(ticker, tmp_data, item, cnt, pattern, "bear", base_path)
                cnt+=1
    except Exception as ex:
        print("error occured", ex)
        pass

def make_chart(ticker, tmp_data, date, idx, pattern, isbull, base_path):

    program_start_time = datetime.today().strftime("%Y%m%d%H%M%S")
    #-2 와 3숫자를 변할수 있다. 특정 차트 패턴이 나오고 앞으로 2일 뒤로 3일을 더해서 이미지를 뽑는다.
    # 저 간격을 줄일수도 있고 늘릴수도 있다. 
    nei_data = tmp_data.iloc[tmp_data.index.get_loc(date) - 2 : tmp_data.index.get_loc(date) + 3]
    mc = mpf.make_marketcolors(up='r',down='b')
    s  = mpf.make_mpf_style(marketcolors=mc)

    flag=""
    if(isbull=="bull"):
        flag = "BULL"
    else:
        flag = "BEAR"

    path = f'{base_path}/{pattern}_{flag}/'
    if not os.path.isdir(path):
        os.mkdir(path)   

    savefig = dict(fname=f'{path}/{program_start_time}_{ticker}_{pattern}_{flag}_{idx}.png',\
    dpi=50,pad_inches=0,bbox_inches='tight')
    #matplotlib 함수
    mpf.plot(nei_data, axisoff=True, type='candle', style=s, savefig=savefig)

def load_csv_and_run(ticker):
    dataset_name = "2016-5year-5days-nasdaq-sector-100"
    try:
        print(f"processing data from {ticker}")
        csv_to_func(ticker, dataset_name)
    except:
        print(f"Error occured at {ticker}")


    #TODO:if done add compress programatically
if __name__ == "__main__":
    #for sector training
    sector_sets = ['Technology', 'Consumer Cyclical', 'Communication Services', 'Financial Services', 'Healthcare',
    'Consumer Defensive', 'Energy', 'Basic Materials', 'Utilities', 'Industrials', 'Real Estate']

    base_path = f'./pattern_datasets/'
    if not os.path.isdir(base_path):
        os.mkdir(base_path)

    #path = "./datasets/daily/"
    path = './datasets/Industrials/'
    tickers = os.listdir(path)
    
    #여러가지 데이터 수집을 위한 폴더의 이름을 임
    #dataset_name = "2016-5year-5days-nasdaqtop300"

    start_time = int(time.time())

    core_count = multiprocessing.cpu_count()
    p = Pool(core_count)
    func = partial(load_csv_and_run)
    p.map(func, tickers)
    p.close()
    p.join()

    #load_csv_and_run(dataset_name)
    end_time = int(time.time())
    

    print("총 작업 시간", (end_time - start_time))

    #sector로 나누고 진행한 코드 아직 분리 못했음 sector분리 코드 사용하려면 daily가 각 섹터 이름으로 바뀌여야함
    # 경로 다 바꾸어 주어야 함 이전 github code 보고 비교할것 / parameter로 변경 진행 안함
    # 

    

    # nohup으로 진행하고 싶으면
    # nohup python preprocessing.py > ./2018-3year-5days-nasdaqtop300-new.log 2>&1&