The purpose of this project is to see if Reinforcement Learning can be useful to train a model to profitably trade crypto. 

Constraints include:
    Fixed:
        -Home computer with a R5 5600x and RTX 3070
    Choosen:  
        -limited to a single trading pair(BTC/USDT)
        -limited to a timeframe(BTC/USDT)

Steps include:
1) Start writing some notes.  
2) download raw data
3) start processing data. 
2) refine datasets and add technical indicators. 
3) use FinRL or other python library to model the 
    -Uses OpenAI Gym envs
4) refine model
5) forward validator analysis 
6) test, grid search and outputs
6) if beats Hold launch papertrader?

carbonZero


1) download raw data
    Got a simple code that downloads OCLHV data from 
        Inputs: 
            (filename, exchange_id, max_retries, symbol, timeframe, since, limit)
            'btc_usdt_15m.csv', 'binance', 3, 'BTC/USDT', '15m', '2018-01-0100:00:00Z', 1000)
        Outputs: