import numpy as np
import pandas as pd


def supperTrend(data, period, multiplier):
    data['highLowDiff'] = data['High'] - data['Low']
    data['highbond'] = abs(data['High'] - data['Close'].shift())
    data['lowbond'] = abs(data['Low'] - data['Close'].shift())

    data.loc[0, 'highLowDiff'] = np.nan
    data.loc[0, 'range'] = np.nan

    data['range'] = data[['highLowDiff', 'highbond', 'lowbond']].max(axis=1)
    data['atr'] = data['range'].rolling(period).mean()

    # basic upperband and lowerband
    data['basicUpperBand'] = (
        (data['High'] + data['Low']) / 2 + (multiplier * data['atr']))
    data['basicLowerBand'] = (data["High"] + data['Low']) / \
        2 - (multiplier * data['atr'])

    # saving dataframe and read
    data.to_csv('file2.csv', header=True, index=True)
    data = pd.read_csv("file2.csv")
    # final LowerBand
    for i, row in data.iterrows():
        if i < period:
            data.loc[i, "finalLowerBand"] = 0.0

        else:
            if (data.loc[i, "basicLowerBand"] > data.loc[i - 1, "finalLowerBand"]) or (
                    data.loc[i - 1, "Close"] < data.loc[i - 1, "finalLowerBand"]):
                data.loc[i, "finalLowerBand"] = data.loc[i, "basicLowerBand"]
            else:
                data.loc[i, "finalLowerBand"] = data.loc[i - 1, "finalLowerBand"]
    # final upperband
    for i, row in data.iterrows():
        if i < period:
            data.loc[i, "finalUpperBand"] = 0.0
        else:
            if (data.loc[i, "basicUpperBand"] < data.loc[i - 1, "finalUpperBand"]) | (
                    data.loc[i - 1, "Close"] > data.loc[i - 1, "finalUpperBand"]):
                data.loc[i, "finalUpperBand"] = data.loc[i, "basicUpperBand"]
            else:
                data.loc[i, "finalUpperBand"] = data.loc[i - 1, "finalUpperBand"]

    # find suppertrend
    for i, row in data.iterrows():
        if i < period:
            data.loc[i, "supperTrend"] = 0.00
        elif (data.loc[i - 1, "supperTrend"] == data.loc[i - 1, "finalUpperBand"]) & (
                data.loc[i, "Close"] <= data.loc[i, "finalUpperBand"]):
            data.loc[i, "supperTrend"] = data.loc[i, "finalUpperBand"]
        elif (data.loc[i - 1, "supperTrend"] == data.loc[i - 1, "finalUpperBand"]) & (
                data.loc[i, "Close"] > data.loc[i, "finalUpperBand"]):
            data.loc[i, "supperTrend"] = data.loc[i, "finalLowerBand"]
        elif (data.loc[i - 1, "supperTrend"] == data.loc[i - 1, "finalLowerBand"]) & (
                data.loc[i, "Close"] >= data.loc[i, "finalLowerBand"]):
            data.loc[i, "supperTrend"] = data.loc[i, "finalLowerBand"]
        elif (data.loc[i - 1, "supperTrend"] == data.loc[i - 1, "finalLowerBand"]) & (
                data.loc[i, "Close"] < data.loc[i, "finalLowerBand"]):
            data.loc[i, "supperTrend"] = data.loc[i, "finalUpperBand"]

    # check buy and sell
    for i, row in data.iterrows():
        if i < period:
            data["Buy_Sell"] = "NA"
        elif (data.loc[i, "supperTrend"] < data.loc[i, "Close"]):
            data.loc[i, "Buy_Sell"] = "Buy"
        else:
            data.loc[i, "Buy_Sell"] = "Sell"

    return data
