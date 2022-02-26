import sys
sys.path.insert(0, './MACROS')
sys.path.insert(1, './src/Modules')
from stockComSymbols import symbols, StockSymbols
from nsepy import get_history
import extract
from datetime import date

def main():
    data= get_history(symbols[StockSymbols.Cipla_Ltd], date(2021, 9, 23), date(2022, 2, 1))
    print(data);
    avg=[];
    months=3;
    weeks=2;
    avg=extract.avgFun(data,weeks,months);
    print(avg);

    mdn= extract.median(data,weeks,months);
    print("median:", mdn)

if __name__ == "__main__":
    main()
