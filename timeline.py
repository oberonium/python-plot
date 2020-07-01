# -*- coding: utf-8 -*-
# ************************************************************#
# FileName      : timeline.py
# Objective     :
# Created by    :
# Created on    : 06/29/2020
# Last modified : 07/01/2020 11:21
# Description   :
#   V1.0 create timeline from xls
# ************************************************************#

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates
from datetime import datetime
#import seaborn as sns


def timeline(xlsfile, output="timeline.png", title="timeline", date_interval=10, figsize=(8.8, 5)):
    alldata = pd.read_excel(xlsfile, header = None, skiprows = 1, dtype = object)
    names = alldata[0]
    dates = alldata[2]

    # Matplotlib fix chinese-font and '-' error
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    #sns.set(font = 'SimHei')
    ## Seaborn chinese-font

    # Convert date strings (e.g. 2014-10-18) to datetime
    dates = [datetime.strptime(d.strftime('%Y-%m-%d'), "%Y-%m-%d") for d in dates]

    # Choose some nice levels
    levels = np.tile([-5, 1, -3, 5, -1, 3],
                     int(np.ceil(len(dates) / 6)))[:len(dates)]

    # Create figure and plot a stem plot with the date
    fig, ax = plt.subplots(figsize =figsize)
    ax.set(title = title)

    markerline, stemline, baseline = ax.stem(dates, levels,
                                             linefmt = "C3-", basefmt = "k-",
                                             use_line_collection = True)

    plt.setp(markerline, mec = "k", mfc = "w", zorder = 3)

    # Shift the markers to the baseline by replacing the y-data by zeros.
    markerline.set_ydata(np.zeros(len(dates)))

    # annotate lines
    vert = np.array(['top', 'bottom'])[(levels > 0).astype(int)]
    for d, l, r, va in zip(dates, levels, names, vert):
        ax.annotate(r, xy = (d, l), xytext = (-3, np.sign(l) * 3),
                    textcoords = "offset points", va = va, ha = "right")

    # format xaxis with 4 month intervals
    ax.get_xaxis().set_major_locator(mdates.MonthLocator(interval = 1))
    ax.get_xaxis().set_major_formatter(mdates.DateFormatter("%b %Y"))
    plt.setp(ax.get_xticklabels(), rotation = 30, ha = "right")
    ax.get_xaxis().set_minor_locator(mdates.DayLocator(interval=date_interval))
    ax.get_xaxis().set_minor_formatter(mdates.DateFormatter("%d"))

    # remove y axis and spines
    ax.get_yaxis().set_visible(False)
    for spine in ["left", "top", "right"]:
        ax.spines[spine].set_visible(False)

    ax.margins(y = 0.1)
    plt.savefig(output, dpi = 600)
    plt.show()
    return


if __name__ == "__main__":
    timeline("timeline-demo.xlsx")
