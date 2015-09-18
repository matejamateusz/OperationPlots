__author__ = 'mmateja'

from PlotLumi import PlotLumi
from PlotMu import PlotMu
from PLOT.PLOT import PLOT
import numpy as np

d=PlotLumi("fillnumber","lumi")

for (key1, value1),(key2,value2) in zip(d.datax.iteritems(),d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot=PLOT(value1,value2)
        plot.setTitle(key1)
        plot.draw()
plot.show()

raw_input("Press enter to continue")