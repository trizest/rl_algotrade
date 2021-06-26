import os 
import pandas as pd
import numpy as np
from datetime import datetime

from pandas.core.frame import DataFrame


exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'

oclhvColumns = ['Unix','Open','Close','Low', 'High','Volume']
finalColumns = []

def readCSV(exchange,pair,timeframe):
    df = pd.read_csv (f'data/fresh/{exchange}/{pair}_{timeframe}.csv', names=oclhvColumns)
    df['Date'] = pd.to_datetime(df['Unix'],unit='ms')
    df = df.set_index('Date')
    df = df[['Unix','Open','Close','Low', 'High','Volume']]
    return df

def pickle(exchange,pair,timeframe,df):
    #IT WENT IN THE JAR HERE!!
    df.to_pickle(f'data/processed/{exchange}/{pair}_{timeframe}.pkl')

def addTechInd(df,indicatorList) :
    do = 'nothing'
    return do

df = readCSV('Binance','btc_usdt','15m')
pickle('Binance','btc_usdt','15m',df)

df.info()
print(df)