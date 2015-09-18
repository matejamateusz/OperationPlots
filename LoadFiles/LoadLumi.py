from __builtin__ import dict

__author__ = 'mmateja'

from LoadFillNumber import LoadFillNumbers
from IO.LumiData import LumiData
import numpy as np
class LoadLumi():

    def __init__(self,fillNumbers):

        self.fillNumbers=fillNumbers
        self.data=LumiData()


    def load(self):
        fillnumber=self.fillNumbers.getFillNumbers()
        self.data.takeFillNumbers(fillnumber)
        for z in range(0, self.fillNumbers.getNumberOfFillNumbers()):  #1 +1
            path = "/home/mmateja/PycharmProjects/OperationPlots/%d/%d_lumi_LHCb.txt" %(fillnumber[z], fillnumber[z])   #/group/online/tfc/LPCfiles/%d/%d_lumi_LHCb.txt
            print path
            d=np.loadtxt(path, delimiter=' ',dtype=[
                ('time_sec', 'float'), ('stablebeams_flag', 'float'), ('lumi', 'float'), ('lumi_err','float'), ('lumi_spec', 'float'), ('lumi_spec_err', 'float')]).T
            self.data.load(path, d)



