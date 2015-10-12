__author__ = 'mmateja'

import numpy as np
from LoadFiles.LoadFillNumber import LoadFillNumbers
from TakeFillNumbers import TakeFillNumbers
import collections
class LPCData(TakeFillNumbers):

    def __init__(self):
        self.data={}

    def load(self,filename, datafromonefile):
        self.data[filename] = datafromonefile

    def getmax_lumi(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            xlist[key]=np.max(value['lumi'])
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['max_lumi'] = xlist.values()
        print ylist
        return ylist

    def getaverage_lumi(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            xlist[key]=np.mean(value['lumi'])
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['average_lumi'] = xlist.values()
        print ylist
        return ylist

    def gettime_hour(self):
        xlist = {}
        for key, value in self.data.iteritems():
            xlist[key]=(value['time_sec']-value['time_sec'][0])/3600
        return xlist

    def getlumi(self):
        xlist = {}
        for key, value in self.data.iteritems():
            xlist[key]=(value['lumi'])
        return xlist

    def gettime_sec(self):
        xlist = {}
        for key, value in self.data.iteritems():
            xlist[key]=(value['time_sec'])
        return xlist

    def gettime_date(self):
        xlist = {}
        ylist = {}
        for key, value in self.data.iteritems():
            xlist[key]=(value['time_sec'][5])
        xlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['time_date']=xlist.values()
        print ylist
        return ylist

    # def getMaxLumi(self):
    #
    #     xlist=[]
    #     v=self.data.values()
    #     for oneFile in v:
    #         xlist.append(oneFile['a'].max)
    #
    #     return np.array(xlist)