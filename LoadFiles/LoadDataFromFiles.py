__author__ = 'mmateja'

from LoadFillNumber import LoadFillNumbers
from LoadFiles import LoadFiles
class LoadDataFromFiles():

    def __init__(self, basic_path, nameFileEnd):
        self.basic_path = basic_path
        self.nameFileEnd = nameFileEnd

    def load(self,pathFillNumbers,name):
        fill=LoadFillNumbers(pathFillNumbers)
        l=LoadFiles(name, fill, self.basic_path, self.nameFileEnd)
        self.data=l.getLoadedFiles().data
    def getData(self):
        return  self.data


