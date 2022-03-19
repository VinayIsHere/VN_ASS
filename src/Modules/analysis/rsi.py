import pandas_ta as pta

def rsi(closeData, timeperiod=14):
    return pta.rsi(closeData['Close'], length= timeperiod)