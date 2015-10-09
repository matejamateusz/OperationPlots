__author__ = 'mmateja'

import numpy as np
from TakeFillNumbers import TakeFillNumbers
import collections
class ConditionData(TakeFillNumbers):

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

    def gettime_sec(self):
        xlist = {}
        for key, value in self.data.iteritems():
            xlist[key]=(value['time_sec'])
        return xlist

    def getpeak_Condition(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            xlist[key]=np.max(value['value'])
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['peak_Condition'] = xlist.values()
        print ylist
        return ylist

    def getaverage_Condition(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            xlist[key]=np.mean(value['value'])
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['average_Condition'] = xlist.values()
        print ylist
        return ylist