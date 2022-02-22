import pandas as pd;
def avgFun(csvfile,week,months):
    sum=0;
    days=week*2;
    avgList=[];
    df=pd.read_csv(csvfile);
    arrProfitAndLoss=list((df["CLOSE"].head(months*30)-df["OPEN"].head(months*30)))
    print(arrProfitAndLoss)
    length=len(arrProfitAndLoss);
    for i in range(length):
        sum+=arrProfitAndLoss[i];
        if i!=0:
            if i%days==0:
                avg=sum/days;
                avgList.append(avg);
                sum=0;
    meanList=avgList;
    return avgList;
