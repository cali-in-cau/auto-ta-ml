import pandas as pd
# from mpl_finance import candlestick2_ohlc
import mplfinance as mpf
import os
import talib

def csv_to_func(ticker, dataset_name):

    base_path = f'./pattern_datasets/{dataset_name}'
    if not os.path.isdir(base_path):
        os.mkdir(base_path)

    patterns_names = talib.get_function_groups()['Pattern Recognition']
    #print(patterns_names)
    csv_data = pd.read_csv(f"./datasets/daily/{ticker}",index_col=0,parse_dates=True)
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

def make_chart(ticker, tmp_data, date, idx, pattern, isbull, base_path):

    #-2 와 3숫자를 변할수 있다. 특정 차트 패턴이 나오고 앞으로 2일 뒤로 3일을 더해서 이미지를 뽑는다.
    # 저 간격을 줄일수도 있고 늘릴수도 있다. 
    nei_data = tmp_data.iloc[tmp_data.index.get_loc(date) - 2 : tmp_data.index.get_loc(date) + 3]
    mc = mpf.make_marketcolors(up='r',down='b')
    s  = mpf.make_mpf_style(marketcolors=mc)

    flag=""
    if(isbull=="bull"):
        flag = "bull"
    else:
        flag = "bear"

    path = f'{base_path}/{pattern}/'
    path_link = [path, path+'bear', path+'bull']
    for x in path_link:
        if not os.path.isdir(x):
            os.mkdir(x)   

    savefig = dict(fname=f'{path}/{flag}/{ticker}_{pattern}_{flag}_{idx}.png',dpi=300,pad_inches=0.25)
    mpf.plot(nei_data,type='candle', style=s, savefig=savefig)

def load_csv_and_run(dataset_name):
    path = "./datasets/daily/"
    tickers = os.listdir(path)
    
    for ticker in tickers:
    #data : csv of 1 ticker
        try:
            print(f"processing data from {ticker}")
            csv_to_func(ticker, dataset_name)
        except e:
            print(f"Error occured at {ticker}")


    #TODO:if done add compress programatically
if __name__ == "__main__":

    base_path = f'./pattern_datasets/'
    if not os.path.isdir(base_path):
        os.mkdir(base_path)
    #여러가지 데이터 수집을 위한 폴더의 이름을 붙임
    dataset_name = "1year-5days-nasdaqtop100"
    load_csv_and_run(dataset_name)