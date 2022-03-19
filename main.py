from MACROS.stockComSymbols import symbols, StockSymbols
from src.Modules.analysis import rsi, macd, superTrend
from src.Modules.statistics import mean, median  
from src.Modules import extract
from nsepy import get_history
from datetime import date

def main():
    data= get_history(symbols[StockSymbols.Cipla_Ltd], date(2022, 1, 1), date(2022, 3, 19))
    # print(data);
    # avg=[];
    # months=3;
    # weeks=2;
    # avg=mean.mean(data,weeks,months);
    # print(avg);
    rsiCal=rsi.rsi(data,14)
    macdCal= macd.macd(data, 12, 26, 9)
    print(rsiCal)
    print("-------------")
    print(macdCal)
    print("-------------")
    #call supertrend wrapper
    
if __name__ == "__main__":
    main()
