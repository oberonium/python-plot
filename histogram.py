# -*- coding: utf-8 -*-
# ************************************************************#
# FileName      : histogram.py
# Objective     :
# Created by    :
# Created on    : 07/03/2020
# Last modified : 07/07/2020 13:59
# Description   :
#   V1.0
# ************************************************************#

import numpy as np
import matplotlib.pyplot as plt


def histogram(plot_data, output, title, label):
    fig, ax = plt.subplots(figsize = (12, 9))
    ax.set_title(title, fontsize = 20)
    ax.set_xlabel("bin", fontsize = 18)
    ax.set_ylabel("frequency", fontsize = 18)

    ax.hist(plot_data, bins = 10, density = True, alpha = 0.5, label = label, rwidth = 0.8)
    #    ax.hist(y, bins=10, density=True, alpha=0.5, label=label2, rwidth=0.8)
    ax.legend(fontsize = 18)

    ax.xaxis.set_tick_params(rotation = 0, labelsize = 18, colors = 'black')
    ax.yaxis.set_tick_params(rotation = 0, labelsize = 18, colors = 'black')

    plt.savefig(output, dpi = 600)
    plt.show()
    return


if __name__ == "__main__":
    N_points = 100000
    # Generate a normal distribution, center at x=0 and y=5
    x = np.random.randn(N_points)
    y = np.random.randn(N_points)

    histogram([x, y], "histo.png", "histogram demo", ("data1", "data2"))
