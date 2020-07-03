# -*- coding: utf-8 -*-
# ************************************************************#
# FileName      : line.py
# Objective     :
# Created by    :
# Created on    : 07/03/2020
# Last modified : 07/03/2020 17:31
# Description   :
#   V1.0 plot line fig
# ************************************************************#

import numpy as np
import matplotlib.pyplot as plt


def lineplot(data, output, title, xlabel, ylabel):
    plot_data = np.loadtxt(data, unpack = True)
    #print(plot_data)

    fig, ax = plt.subplots(figsize = (15, 5))
    ax.set_title(title, fontsize =18)
    ax.set_xlabel(xlabel, fontsize = 18, fontfamily = 'sans-serif')#, fontstyle = 'italic')
    ax.set_ylabel(ylabel, fontsize = 18)#, fontstyle='oblique')

    #ax.set_aspect('equal')
    ax.minorticks_on()
    ax.plot(plot_data[0], plot_data[1])
    #ax.set_xlim(0,16)
    #ax.grid(which = 'major', axis = 'both')

    ax.xaxis.set_tick_params(rotation=0, labelsize=18, colors='black')
    ax.yaxis.set_tick_params(rotation=0, labelsize=18, colors='black')
    ax.tick_params(which = 'both', width = 1)
    ax.tick_params(which = 'major', length = 7)
    ax.tick_params(which = 'minor', length = 4, color = 'black')
    #start, end = ax.get_xlim()
    #ax.xaxis.set_ticks(np.arange(0, 16000, 1000))
    #ax.yaxis.tick_right()

    plt.savefig(output, dpi = 600)
    plt.show()
    return


if __name__ == "__main__":
    lineplot("line.txt", "line.png", "loss", "iteration", "loss")
