import os 
import pandas as pd
from finta import TA
import numpy as np
from datetime import datetime

from pandas.core.frame import DataFrame


exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'

oclhvColumns = ['Unix','Open','Close','Low', 'High','Volume']
finalColumns = []

def read_CSV(exchange,pair,timeframe):
    df = pd.read_csv (f'data/fresh/{exchange}/{pair}_{timeframe}.csv', names=oclhvColumns)
    df['Date'] = pd.to_datetime(df['Unix'],unit='ms')
    df = df.set_index('Date')
    df = df[['Unix','Open','Close','Low', 'High','Volume']]
    return df

def add_tech_ind(df) :
    df['SMA12'] = TA.SMA(df, 12)
    df['SMA21'] = TA.SMA(df, 21)
    df['SMA55'] = TA.SMA(df, 55)
    df['SMA100'] = TA.SMA(df, 100)
    df['RSI'] = TA.RSI(df)
    df['OBV'] = TA.OBV(df)
    return df


def pickle_df(exchange,pair,timeframe,df):
    #IT WENT IN THE JAR HERE!!
    df.to_pickle(f'data/processed/{exchange}/{pair}_{timeframe}.pkl')
    print(f'data/processed/{exchange}/{pair}_{timeframe}.pkl')




if __name__ == '__main__':
    df = read_CSV('Binance','btc_usdt','15m')
    df = add_tech_ind(df)
    pickle_df('Binance','btc_usdt','15m',df)

    df.info()
    print(df.head(1))
