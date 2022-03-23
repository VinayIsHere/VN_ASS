from MACROS.stockComSymbols import symbols, StockSymbols, micros
from src.Modules.analysis import rsi, macd, superTrend
from src.Modules.statistics import mean, median
from src.Modules import extract
from nsepy import get_history
from datetime import date
from src.Modules.plotting import plotting


def main():
    data = get_history(symbol='IRCTC',
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

    rsiCal = rsi.rsi(data, 14)

    #macdCal= macd.macd(data, 12, 26, 9)
    """supertrendval, supertrendBuysell = superTrend.supperTrend(
        data, 14, micros.multiplier.value)
    print(rsiCal)
    print("-------------")
    # print(macdCal)
    print("-------------")
    print(supertrendval, supertrendBuysell)
    """  # call supertrend wrapper

    # call Plotting
    plotting.figplot(data, rsiCal)


if __name__ == "__main__":
    main()
