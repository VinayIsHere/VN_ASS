def rsi(data, days):
    delta = data['Close'].diff(1).dropna()

    # delta.dropna(inplace=True)

    positive = delta.copy()

    negative = delta.copy()

    positive[positive < 0] = 0

    negative[negative > 0] = 0

    days = days

    #  all the other days of range will give nan and required will give required output print(positive.rolling(days).mean())

    avg_gain = abs(positive.rolling(window=days).mean().fillna(0))

    # print(avg_gain)

    avg_loss = abs(negative.rolling(window=days).mean().fillna(0))

    # print(avg_loss)

    relative_strenght = avg_gain/avg_loss

    # print(relative_strenght)

    RSI = 100.0-(100.0/(1+relative_strenght))

    return RSI
