import pandas_ta as pTa

def superTrend(high, low, close, Period, Multiplier):
    return pTa.supertrend(high, low, close, Period, Multiplier)