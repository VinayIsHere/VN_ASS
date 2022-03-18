import pandas_ta as pta
# def closepricelist(dataframe,days):
#     closeList = list((dataframe["Close"].head(days+1)))
#     change=[]
#     up_moves=[]
#     down_moves=[]
#
#     for i in range(1,len(closeList),1):
#         change.append(closeList[i]-closeList[i-1])
#         try:
#             if(change[i]>0):
#                 up_moves.append(change[i]);
#             elif(change[i]<=0):
#                 up_moves.append(0);
#
#
#
#             elif(change[i]<0):
#                 down_moves[abs(change[i])]
#             elif(change[i]>=0):
#                 down_moves.append(0);
#         except:
#             pass
#     avgU_avgD(up_moves,down_moves)
#
#
# def avgU_avgD(up_moves,down_moves):
#     up_moves_sum=0;
#     down_moves_sum=0;
#     for _ in up_moves:
#         up_moves_sum=up_moves_sum+_;
#     for _ in down_moves:
#         down_moves_sum=down_moves_sum+_;
#     AvgU=up_moves_sum/len(up_moves);
#     AvgD=down_moves_sum/len(down_moves);
#     relativeStrength(AvgU,AvgD)
#
# def relativeStrength(AvgUp,AvgDown):
#
#     RS=AvgUp/AvgDown
#     RSI(RS);
#
# def RSI(RS):
#     rsi=100-(100/(1+RS));
#     return rsi;

def RSI_pandas_ta(dataframe,timeperiod):
    RSI=pta.rsi(dataframe['Close'],length=timeperiod)
    return RSI;





