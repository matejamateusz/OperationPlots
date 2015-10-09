__author__ = 'mmateja'

from PlotLPC import PlotLPC
from PlotCondition import PlotCondition
from PLOT.PLOT import PLOT, dateformat
import numpy as np
from datetime import datetime

basic_path = "/home/mmateja/PycharmProjects/OperationPlots/"
#nameFileEnd = "Mu"


startfillnumber = 3819
endfillnumber = 4000

xaxis = "time_sec"
yaxis = "lumi"
d=PlotLPC(xaxis, yaxis, basic_path, "lumi_LHCb", startfillnumber, endfillnumber)
#d=PlotCondition("time_year","value", basic_path, nameFileEnd)
for (key1, value1),(key2,value2) in zip(d.datax.iteritems(),d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        #value1 = [datetime.fromtimestamp(v1) for v1 in value1]
        if "time_sec" or "time" in (xaxis, yaxis):
            value1 = dateformat(value1)
            plot=PLOT(value1, value2)
            plot.setTitle(key1) #key1
            plot.setDate()
            plot.draw()
        else:
            plot=PLOT(value1, value2)
            plot.setTitle(key1) #key1
            plot.draw()
plot.show()
raw_input("Press enter to continue")