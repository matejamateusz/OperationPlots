__author__ = 'mmateja'

from LoadFillNumber import LoadFillNumbers
from LoadFiles import LoadFiles
class LoadDataFromFiles():



    def load(self,pathFillNumbers,name):

        fill=LoadFillNumbers(pathFillNumbers)
        l=LoadFiles(name, fill)
        self.data=l.getLoadedFiles().data
    def getData(self):
        return  self.data


