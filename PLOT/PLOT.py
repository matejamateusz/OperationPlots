__author__ = 'mmateja'
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.dates as mdates
from datetime import datetime
import numpy as np


def dateformat(value1):
        value1 = [datetime.fromtimestamp(v1) for v1 in value1]
        return value1

class PLOT:
    def __init__(self, x, y):
        self.x = x#.astype(datetime)
        self.y = y
        self.figure = plt.figure()

        self.ax = plt.subplot(111)
        self.ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')
        #self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))

        self.figure.suptitle("LHCB")
        self.xlabel = "Date"
        self.ylabel = 'Peak Inst Luminosity (10^24/cm^2*s^1)'

        self.y_min = 0
        self.y_max = 1

        self.color = 'b'
        self.markersize = 10
        self.linestyle = 'None'
        self.marker = Line2D.filled_markers[0]
        plt.grid()
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)



    def show(self):
        plt.tight_layout()
        plt.show()

    def draw(self):
        #plt.xticks(rotation=45)# horizontalalignment='right')
        plt.plot(self.x, self.y, marker=self.marker, linestyle=self.linestyle, color=self.color,
                 markersize=self.markersize)

    def sety_min(self, y_min):
        self.y_min = y_min
        plt.ylim(self.y_min, self.y_max)


    def setTitle(self, title):

        self.setTitle=title
        self.figure.suptitle(self.setTitle)

    def setDate(self):
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.xticks(rotation=45)# horizontalalignment='right')

    def setxlabel(self, xlabel):
        self.xlabel = xlabel

    def setylabel(self, ylabel):
        self.ylabel = ylabel

    def disableGrid(self):
        plt.grid(False)

    def setShape(self, shape):
        self.style[1] = shape

    def setMarkerSize(self, size):
        self.markersize = size

    def setColor(self, color):
        self.color = color

    def setMarkerType(self, numberOfMarker):
        self.marker = Line2D.filled_markers[numberOfMarker]

    def setlineStyle(self, style):
        self.linestyle = style