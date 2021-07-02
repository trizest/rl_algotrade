
import pandas as pd
from finta import TA

test = 1

exchange = 'Binance'
pair = 'btc_usdt'
timeframe = '15m'
oclhvColumns = ['Unix', 'Open', 'Close', 'Low', 'High', 'Volume']



def read_csv(ex, p, tf):
    d_f = pd.read_csv(f'data/fresh/{ex}/{p}_{tf}.csv', names=oclhvColumns)
    d_f['Date'] = pd.to_datetime(d_f['Unix'], unit='ms')
    d_f = d_f.set_index('Date')
    d_f = d_f[['Unix', 'Open', 'Close', 'Low', 'High', 'Volume']]
    return d_f


def add_tech_ind(d_f):
    d_f['SMA12'] = TA.SMA(d_f, 12)
    d_f['SMA21'] = TA.SMA(d_f, 21)
    d_f['SMA55'] = TA.SMA(d_f, 55)
    d_f['SMA100'] = TA.SMA(d_f, 100)
    d_f['RSI'] = TA.RSI(d_f)
    d_f['OBV'] = TA.OBV(d_f)
    return d_f


def pickle_df(ex, p, tf, d_f):
    # IT WENT IN THE JAR HERE!!
    d_f.to_pickle(f'data/processed/{ex}/{p}_{tf}.pkl')
    print(f'data/processed/{ex}/{p}_{tf}.pkl')


if __name__ == '__main__':
    df = read_csv(exchange, pair, timeframe)
    df = add_tech_ind(df)
    pickle_df(exchange, pair, timeframe, df)

    df.info()
    print(df.head(1))
