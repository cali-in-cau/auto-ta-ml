import os
import yfinance as yf


category = {}
category_record = {}
print("--start--")
with open("datasets/nasdaq.csv") as f:
    
    for line in f:
        if "," not in line:
            continue
        symbol = line.split(",")[0]
        #print(symbol)
        try:
            tickerdata = yf.Ticker(symbol)
            sector = tickerdata.info['sector']
            
            if sector not in category.keys():
                category[sector] = 1
                category_record[sector] = [symbol]
            else:
                category[sector] += 1
                category_record[sector].append(symbol)
        except Exception as ex:
            #print(ex)
            pass
                
    print(category)
    print(category_record)
print("--end--")