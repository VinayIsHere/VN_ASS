import pandas_ta as pta
def closepricelist(dataframe,days):
    closeList = list((dataframe["Close"].head(days+1)))
    change=[]
    up_moves=[]
    down_moves=[]
    print(f"close {closeList}")

    for i in range(1,len(closeList),1):
        change.append(closeList[i]-closeList[i-1])
    for i in range(len(change)):

        if(change[i]>0):
            up_moves.append(change[i]);

        if(change[i]<=0):
            up_moves.append(0);



        if(change[i]<0):
            down_moves.append(abs(change[i]))
        if(change[i]>=0):
            down_moves.append(0);


    print(f"change{change}")
    print(f"up{up_moves}")
    print(f"down{down_moves}")
    rsi=avgU_avgD(up_moves, down_moves)
    return rsi

def avgU_avgD(up_moves,down_moves):
    up_moves_sum=0;
    down_moves_sum=0;
    for _ in up_moves:
        up_moves_sum=up_moves_sum+_;
    for _ in down_moves:
        down_moves_sum=down_moves_sum+_;
    print(f"upmoves sum{up_moves_sum}")
    print(f"downmoves sum{down_moves_sum}")
    AvgU=up_moves_sum/len(up_moves);
    AvgD=down_moves_sum/len(down_moves);
    print(f"AVGup{AvgU}")
    print(f"AVGud{AvgD}")
    rsi=relativeStrength(AvgU,AvgD)
    return rsi

def relativeStrength(AvgUp,AvgDown):

    RS=AvgUp/AvgDown
    print(f"rs{RS}")
    rsi=RSI(RS);
    return rsi


def RSI(RS):
    rsi=100-(100/(1+RS));
    return  rsi;


def RSI_pandas_ta(dataframe,timeperiod):
    RSI=pta.rsi(dataframe['Close'],length=timeperiod)
    return RSI;





