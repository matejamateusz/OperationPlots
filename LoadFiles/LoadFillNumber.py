__author__ = 'mmateja'
import numpy as np

class LoadFillNumbers():

    def __init__(self,pathOfFillNumbersFile):
        self.fillnumber = np.loadtxt(pathOfFillNumbersFile)

    def getFillNumbers(self):

        return self.fillnumber
    def getNumberOfFillNumbers(self):

        return self.fillnumber.size