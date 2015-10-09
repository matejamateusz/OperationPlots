from __builtin__ import dict

__author__ = 'mmateja'

from LoadFillNumber import LoadFillNumbers
from IO.LPCData import LPCData
import numpy as np
class LoadLPC():

    def __init__(self, fillNumbers, basic_path, nameFileEnd):

        self.fillNumbers=fillNumbers
        self.data=LPCData()
        self.basic_path = basic_path
        self.nameFileEnd = nameFileEnd

    def load(self):
        fillnumber = self.fillNumbers.getFillNumbers()
        print fillnumber
        self.data.takeFillNumbers(fillnumber)
        for z in range(0, self.fillNumbers.getNumberOfFillNumbers()):  #1 +1
            path = self.basic_path + "/%d/%d_%s.txt" %(fillnumber[z], fillnumber[z], self.nameFileEnd)   #/group/online/tfc/LPCfiles/%d/%d_lumi_LHCb.txt
            print path
            d=np.loadtxt(path, delimiter=' ', dtype=[
                ('time_sec', 'float'), ('stablebeams_flag', 'float'), ('lumi', 'float'), ('lumi_err','float'), ('lumi_spec', 'float'), ('lumi_spec_err', 'float')]).T
            self.data.load(path, d)



