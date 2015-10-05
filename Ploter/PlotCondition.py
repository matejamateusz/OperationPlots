from  Plot import Plot

from LoadFiles.LoadFiles import LoadFiles
from LoadFiles.LoadDataFromFiles import LoadDataFromFiles
from PLOT.PLOT import PLOT
class PlotCondition(Plot):


    def __init__(self,x,y):
        Plot.__init__(self,x,y)

        loader=LoadDataFromFiles()
        loader.load("/home/mmateja/PycharmProjects/OperationPlots/Fillnumbers.txt","mu")
        dataObject=loader.getData()

        self.datax=eval("dataObject.get"+x+"()")
        self.datay=eval("dataObject.get"+y+"()")

    def getData(self):
        return  self.datax,self.datay


