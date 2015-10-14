__author__ = 'mmateja'


class RetrieveDataForPlot:

    def __init__(self,dataObject):
        self.dataObject=dataObject

    def retrieveData(self,xaxis,yaxis):

        self.datax=eval("self.dataObject.get"+xaxis+"()")
        self.datay=eval("self.dataObject.get"+yaxis+"()")

        return  self.datax,self.datay