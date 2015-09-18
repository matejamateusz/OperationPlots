__author__ = 'mmateja'

import numpy as np
from FillnumberData import TakeFillNumber
class MuData(TakeFillNumber):

    def __init__(self):
        self.data={}


    def load(self, filename, datafromonefile):
        self.data[filename] = datafromonefile

    def getvalue(self):
        xlist = {}
        for key, value in self.data.iteritems():
            xlist[key]=(value['value'])
        return xlist

    def gettime_year(self):
        xlist = {}
        for key, value in self.data.iteritems():
            xlist[key]=(value['time_year'])
        return xlist
