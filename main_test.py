__author__ = 'mmateja'
__author__ = 'mmateja'

from Ploter.PlotLPC import PlotLPC
from Ploter.PlotCondition import PlotCondition
from PLOT.PLOT import PLOT, dateformat
from RetrieveData.RetrieveDataForPlot import RetrieveDataForPlot
from RetrieveData.Retriever import Retriever
import numpy as np
from datetime import datetime

basic_path = "/home/mmateja/PycharmProjects/OperationPlots/"
#nameFileEnd = "Mu"


startfillnumber = 3819
endfillnumber = 4000
##################################################TEMPLATE PLOTTING################################################
# xaxis = "fillnumber"  #TIME_DATE, FILLNUMBER
# yaxis = "max_lumi"
# d=PlotLPC(xaxis, yaxis, basic_path, "lumi_LHCb", startfillnumber, endfillnumber)
# #d=PlotCondition("time_year","value", basic_path, nameFileEnd)
# for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
#         #value1 = [datetime.fromtimestamp(v1) for v1 in value1]
#         if key1 != key2 and ("time_sec" and "lumi" in xaxis and yaxis):
#             print "ERROR DIFFERENT KEYS!!!!!!!"
#         if "time_date" in xaxis and yaxis:
#             value1 = dateformat(value1)
#             plot=PLOT(value1, value2)
#             plot.setTitle(key1) #key1
#             plot.setDate()
#             plot.draw()
#         else:
#             plot=PLOT(value1, value2)
#             plot.setTitle(key1) #key1
#             plot.draw()
#
######################################################################################################################
d = Retriever( basic_path, "lumi_LHCb", startfillnumber, endfillnumber)
data = d.retrieve("LPC") #LPC, CONDITION
r = RetrieveDataForPlot(data)
datax,datay=r.retrieveData("fillnumber","max_lumi")
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot=PLOT(value1, value2)
        plot.setTitle("LHCb Peak Instantaneous Lumi at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Inst Luminosity (10^24/cm^2*s^1)")
        plot.draw()
datax,datay=r.retrieveData("fillnumber","average_lumi")
for (key1, value1),(key2, value2) in zip(datax.iteritems(), datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot=PLOT(value1, value2)
        plot.setTitle("LHCb Peak Instantaneous Lumi at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Inst Luminosity (10^24/cm^2*s^1)")
        plot.draw()



xaxis = "time_date"  #TIME_DATE, FILLNUMBER
yaxis = "average_lumi"
d=PlotLPC(xaxis, yaxis, basic_path, "lumi_LHCb", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        value1 = dateformat(value1)
        plot=PLOT(value1, value2)
        plot.setDate()
        plot.setTitle("LHCb Peak Instantaneous Lumi at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("Date")
        plot.setylabel("Average Inst Luminosity (10^24/cm^2*s^1)")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015AvgLumiTime.png")


xaxis = "fillnumber"  #TIME_DATE, FILLNUMBER
yaxis = "max_condition"
d=PlotCondition(xaxis, yaxis, basic_path, "Mu", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot = PLOT(value1, value2)
        plot.setTitle("LHCb Peak Mu at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Mu")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015PeakMuFill.png")

xaxis = "time_date"  #TIME_DATE, FILLNUMBER
yaxis = "max_condition"
d=PlotCondition(xaxis, yaxis, basic_path, "Mu", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        value1 = dateformat(value1)
        plot = PLOT(value1, value2)
        plot.setDate()
        plot.setTitle("LHCb Peak Mu at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("Date")
        plot.setylabel("Peak Mu")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015PeakMuTime.png")

xaxis = "fillnumber"  #TIME_DATE, FILLNUMBER
yaxis = "average_condition"
d=PlotCondition(xaxis, yaxis, basic_path, "Mu", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot = PLOT(value1, value2)
        plot.setTitle("LHCb Average Mu at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Average Mu")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015AverageMuFill.png")

xaxis = "time_date"  #TIME_DATE, FILLNUMBER
yaxis = "average_condition"
d=PlotCondition(xaxis, yaxis, basic_path, "Mu", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        value1 = dateformat(value1)
        plot = PLOT(value1, value2)
        plot.setDate()
        plot.setTitle("LHCb Average Mu at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("Date")
        plot.setylabel("Average Mu")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015AverageMuTime.png")

xaxis = "fillnumber"  #TIME_DATE, FILLNUMBER
yaxis = "max_condition"
d=PlotCondition(xaxis, yaxis, basic_path, "Pileup", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot = PLOT(value1, value2)
        plot.setTitle("LHCb Peak Pileup at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Peak Pileup")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015PeakPileupFill.png")

xaxis = "time_date"  #TIME_DATE, FILLNUMBER
yaxis = "max_condition"
d=PlotCondition(xaxis, yaxis, basic_path, "Pileup", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        value1 = dateformat(value1)
        plot = PLOT(value1, value2)
        plot.setDate()
        plot.setTitle("LHCb Peak Pileup at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("Date")
        plot.setylabel("Peak Pileup")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015PeakPileupTime.png")

xaxis = "fillnumber"  #TIME_DATE, FILLNUMBER
yaxis = "average_condition"
d=PlotCondition(xaxis, yaxis, basic_path, "Pileup", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        plot = PLOT(value1, value2)
        plot.setTitle("LHCb Average Pileup at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("LHC Fillnumber")
        plot.setylabel("Average Pileup")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015AveragePileupFill.png")

xaxis = "time_date"  #TIME_DATE, FILLNUMBER
yaxis = "average_condition"
d=PlotCondition(xaxis, yaxis, basic_path, "Pileup", startfillnumber, endfillnumber)
for (key1, value1),(key2, value2) in zip(d.datax.iteritems(), d.datay.iteritems()): #-key2,0iteritems ze wzgledu na typy danych
        value1 = dateformat(value1)
        plot = PLOT(value1, value2)
        plot.setDate()
        plot.setTitle("LHCb Average Pileup at p-p 6.5 TeV in 2015") #key1
        plot.setxlabel("Date")
        plot.setylabel("Average Pileup")
        plot.draw()
        plot.savefig("OUTPUTPLOTS/2015AveragePileupTime.png")





#plot.show()
#raw_input("Press enter to continue")
