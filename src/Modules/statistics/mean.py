import pandas as pd;
import numpy as np;
import scipy as sp;

def avgFun(dataframe,week,months):
    sum=0;
    days=week*7;
    avgList=[];
    arrProfitAndLoss=list((dataframe["Close"].head(months*30)-dataframe["Open"].head(months*30)))
    length=len(arrProfitAndLoss);
    for i in range(length):
        sum+=arrProfitAndLoss[i];
        if i!=0:
            if i%days==0:
                avg=sum/days;
                avgList.append(avg);

                sum=0;

    return avgList;