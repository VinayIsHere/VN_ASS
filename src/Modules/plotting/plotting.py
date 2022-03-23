import pandas as pd
import mplcursors
import matplotlib.pyplot as plt


def figplot(data, RSI):

    combined = pd.DataFrame()

    combined['Close'] = data['Close']
    combined['RSI'] = RSI

    # plotting

    fig = plt.figure(figsize=(12, 8))

    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212, sharex=ax1)

    # main
    ax1.plot(combined.index, combined['Close'], color='red')
    ax1.set_title(data['Symbol'][1], color='blue')

    ax1.grid(True, color='#555555')
    ax1.set_axisbelow(True)
    ax1.set_facecolor('black')
    ax1.figure.set_facecolor('#121212')
    ax1.tick_params(axis='x', colors='white')
    ax1.tick_params(axis='y', colors='white')

    # RSI Plotting
    ax2.plot(combined.index, combined['RSI'], color='yellow')

    # threshold
    b_th = 40
    a_th = 70

    ab_th = combined['RSI'] > a_th
    bw_th = combined['RSI'] < b_th

    ax2.scatter(combined.index[bw_th], combined['RSI'][bw_th], color='green')

    ax2.scatter(combined.index[ab_th], combined['RSI'][ab_th], color='red')

    ax2.axhline(0, linestyle='--', alpha=0.5, color='#ff0000')
    ax2.axhline(10, linestyle='--', alpha=0.5, color='#ffaa00')
    ax2.axhline(20, linestyle='--', alpha=0.5, color='#00ff00')
    ax2.axhline(30, linestyle='--', alpha=0.5, color='#cccccc')
    ax2.axhline(70, linestyle='--', alpha=0.5, color='#cccccc')
    ax2.axhline(80, linestyle='--', alpha=0.5, color='#00ff00')
    ax2.axhline(90, linestyle='--', alpha=0.5, color='#ffaa00')
    ax2.axhline(100, linestyle='--', alpha=0.5, color='#ff0000')

    ax2.set_title('RSI Value', color='yellow')
    ax2.grid(False)
    ax2.set_axisbelow(True)
    ax2.set_facecolor('black')
    ax2.figure.set_facecolor('#121212')
    ax2.tick_params(axis='x', colors='white')
    ax2.tick_params(axis='y', colors='white')

    index = len(combined.index)-1
    # label code

    ax1.text(combined.index[index],  combined['Close'][index],
             combined['Close'][index], size=12, color='white')

    ax2.text(combined.index[index],  combined['RSI'][index],
             "{:.2f}".format(combined['RSI'][index]), size=12, color='white')

    mplcursors.cursor(hover=True)

    plt.subplots_adjust(left=0.04,
                        bottom=0.05,
                        right=0.99,
                        top=0.9,
                        wspace=0.2,
                        hspace=0.4)
    # plt.subplot_tool()
    # fig.tight_layout()

    plt.show()
