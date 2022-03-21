import pandas as pd;
import numpy as np;
import scipy as sp;

def median(dataframe,week,months):
    arrProfitAndLoss = list((dataframe["Close"].head(months * 30) - dataframe["Open"].head(months * 30)))
    length = len(arrProfitAndLoss);
    days=week*7
    median=[]
    for i in range(length):
        temp = []
        temp.append(arrProfitAndLoss[i]);
        if i!=0:
            if i%days==0:
                medn=np.median(temp)
                median.append(medn);
    return  median
