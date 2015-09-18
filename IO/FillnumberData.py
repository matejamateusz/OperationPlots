__author__ = 'mmateja'
import collections
class TakeFillNumber():

    def takeFillNumbers(self, fillnumber):
        self.fillnumber = fillnumber

    def getfillnumber(self):
        xlist = {}
        ylist = {}
        for z in self.fillnumber:
            xlist[z]=z #ścieżka
        zlist = collections.OrderedDict(sorted(xlist.items()))
        ylist['fillnumbers']=[3819,3820,3824]
        print ylist
        return ylist