from MACROS.stockComSymbols import symbols, StockSymbols, micros
from src.Modules.analysis import rsi, macd, superTrend, s
from src.Modules.statistics import mean, median
from src.Modules import extract
from nsepy import get_history
from datetime import date
from src.Modules.plotting import plotting


def main():
    data = get_history(symbol='SBIN',
                       start=date(2022, 2, 1),
                       end=date.today())

    """data = get_history(symbols[StockSymbols.Cipla_Ltd],
                       date(2022, 1, 1), date(2022, 3, 19))"""

    # print(data)
    # avg=[];
    # months=3;
    # weeks=2;
    # avg=mean.mean(data,weeks,months);
    # print(avg);

    # rsi=rsiCal.RSI_pandas_ta(data,14)

    data['st'], data['upt'], data['dt'], = s.get_supertrend(
        data['High'], data['Low'], data['Close'], 10, 3)
    # print(data)
    rsidata = data.copy()
    rsiCal = rsi.rsi(rsidata, 14)
    plotting.figplot(rsidata, rsiCal)

    # macdCal= macd.macd(data, 12, 26, 9)"

    """
    print(rsiCal)
    print("-------------")
    # print(macdCal)
    print("-------------")

    """  # call supertrend wra
    # print(supertrendBuysell)
    # call Plotting


if __name__ == "__main__":
    main()
