from MACROS.stockComSymbols import symbols, StockSymbols
from src.Modules.analysis import rsi, macd, superTrend
from src.Modules.statistics import mean, median  
from src.Modules import extract
from nsepy import get_history
from datetime import date

def main():
<<<<<<< HEAD
    data = get_history(symbol='IRCTC',
                       start=date(2022, 2, 1),
                       end=date.today())
=======
    data= get_history(symbols[StockSymbols.Cipla_Ltd], date(2022, 1, 1), date(2022, 3, 19))
>>>>>>> Data-_Extraction
    # print(data);
    # avg=[];
    # months=3;
    # weeks=2;
    # avg=mean.mean(data,weeks,months);
    # print(avg);
<<<<<<< HEAD
    # rsi=rsiCal.RSI_pandas_ta(data,14)
    rsi=rsiCal.closepricelist(data,14)
    print(rsi);


=======
    rsiCal=rsi.rsi(data,14)
    macdCal= macd.macd(data, 12, 26, 9)
    print(rsiCal)
    print("-------------")
    print(macdCal)
    print("-------------")
    #call supertrend wrapper
    
>>>>>>> Data-_Extraction
if __name__ == "__main__":
    main()
