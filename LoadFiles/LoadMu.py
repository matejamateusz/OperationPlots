__author__ = 'mmateja'

from LoadFillNumber import LoadFillNumbers
from IO.MuData import MuData
import numpy as np
class LoadMu():

    def __init__(self,fillNumbers):

        self.fillNumbers=fillNumbers
        self.data=MuData()


    def load(self):
        fillnumber=self.fillNumbers.getFillNumbers()
        for z in range(0, self.fillNumbers.getNumberOfFillNumbers()):  #1 +1
            path = "/home/mmateja/PycharmProjects/OperationPlots/%d/%d_Mu.txt" %(fillnumber[z], fillnumber[z])   #/group/online/tfc/ROOT/RunParameters/%d_Mu.txt
            print path
            d=np.loadtxt(path, delimiter=' ',dtype=[
                ('time_year', 'float'), ('time_month_flag', 'float'), ('time_day', 'float'), ('time_hours', 'float'),
                ('time_minute', 'float'), ('time_second', 'float'), ('value', 'float')]).T
            self.data.load(path, d)



