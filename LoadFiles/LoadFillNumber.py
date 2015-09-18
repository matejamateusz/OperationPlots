__author__ = 'mmateja'
import numpy as np

class LoadFillNumbers():

    def __init__(self,pathOfFillNubersFile):
        self.fillnumber = np.loadtxt(pathOfFillNubersFile)

    def getFillNumbers(self):

        return self.fillnumber
    def getNumberOfFillNumbers(self):

        return self.fillnumber.size