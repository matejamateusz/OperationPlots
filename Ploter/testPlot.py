__author__ = 'mmateja'

from PlotLPC import PlotLPC
from PlotCondition import PlotCondition
from PLOT.PLOT import PLOT
import numpy as np

basic_path = "/home/mmateja/PycharmProjects/OperationPlots/"

nameFileEnd = "lumi_LHCb"


d=PlotLPC("time_sec","lumi", basic_path, nameFileEnd)
#d=PlotCondition("time_year","value", basic_path, nameFileEnd)
for (key1, value1),(key2,value2) in zip(d.datax.iteritems(),d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot=PLOT(value1,value2)
        plot.setTitle(key1) #key1
        plot.draw()
plot.show()

raw_input("Press enter to continue")