import pandas as pd;
import numpy as np;
import scipy as sp;

def calCulateProfitAndLoss(dataframe, months):
    return list((dataframe["Close"].head(months*30)-dataframe["Open"].head(months*30)))

def avgFun(dataframe,week,months):
    sum=0;
    days=week*7;
    avgList=[];
    arrProfitAndLoss= calCulateProfitAndLoss(dataframe, months)

    length=len(arrProfitAndLoss);
    
    sum=0   
    for i in range(1, length+1):
        sum+=arrProfitAndLoss[i-1];
        
        if(i%days == 0):
            avgList.append(sum/days)
            sum=0

    return avgList;


def median(dataframe,week,months):
    arrProfitAndLoss = calCulateProfitAndLoss(dataframe, months)
    length = len(arrProfitAndLoss);
    days=week*7
    median=[]
    for i in range(1,length+1, 14):
        temp = []
        temp.extend(arrProfitAndLoss[i-1: i-1+14]);
        #numpy will do the sorting by itself
        medn=np.median(temp)
        median.append(medn);
        

    return  median






