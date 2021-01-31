# Auto-TA-ML
## Authors
TBA
## Summary
2021 people space group c
## Prerequisites
    * python3 (tested on 3.8.5)
    * recommend making a virtual environemnt
## Module Install
## Actual Install
if this do not work, look at `requirements.txt`

```sh
pip install yfinance
pip install matplotlib
pip install --upgrade mplfinance
#사용하고 있는 mplfinance 버전은 mplfinance==0.12.7a4 입니다.
```
```sh
# for TA-Lib
pip install TA-Lib
# https://mrjbq7.github.io/ta-lib/install.html 
# 설치 안되면 위 링크에 설치 방법 있음 
```
## Execute
* download_ohlc_csv.py
```sh
# excute on terminal or shell
python download_ohlc_csv.py
```
This will download OHLC data from yahoo finance apis, There are Ticker csv, so you can use it. 

(2021-01-25) in this version you have to make daily folder to download csv data from tickers. 

* ohlc_to_image.py
```sh
# excute on terminal or shell
python ohlc_to_image.py
```
This will change from OHLC data(you have to download or get data first. look at download_ohlc_csv.py) to candle stick/line graph and save into png file. read the function parameter descriptions below before you excute.

* preprocessing.py
```sh
# excute on terminal or shell
python ohlc_to_image.py
```
With TAlib[https://mrjbq7.github.io/ta-lib/] we tag chart patterns automatically. and we make images with the data of OHLC, chart pattern(label). The image will contain the data with date when the chart pattern detected, including the date before and after the pattern appears.(you can change the period(function parameter))

(2021-01-25) you have to make "tmp" folder to execute. read the `preprocessing.py`

## License
TBA

## TODO
- [] 병렬처리 속도 향상
- [X] imagepid값 다시 부여
- [x] 폴더 재구성
- [] 이미지 dropout
- [] 불필요한 정보 빼기