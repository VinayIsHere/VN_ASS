import sys
sys.path.insert(0, '/home/noor/Desktop/VN_ASS/MACROS')
sys.path.insert(1, '/home/noor/Desktop/VN_ASS/src/Modules')
from stockComSymbols import symbols, StockSymbols
from nsepy import get_history
import extract
import src.Modules.rsicalculation as rsiCal
from datetime import date

def main():
    data = get_history(symbol='IRCTC',
                       start=date(2022, 2, 1),
                       end=date.today())
    # print(data);
    # avg=[];
    # months=3;
    # weeks=2;
    # avg=extract.avgFun(data,weeks,months);
    # print(avg);
    # rsi=rsiCal.RSI_pandas_ta(data,14)
    rsi=rsiCal.closepricelist(data,14)
    print(rsi);


if __name__ == "__main__":
    main()