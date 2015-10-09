__author__ = 'mmateja'

from LoadFillNumber import LoadFillNumbers
from IO.ConditionData import ConditionData
import numpy as np
class LoadCondition():

    def __init__(self,fillNumbers, basic_path, nameFileEnd):

        self.fillNumbers=fillNumbers
        self.data=ConditionData()
        self.basic_path = basic_path
        self.nameFileEnd = nameFileEnd

    def load(self):
        fillnumber=self.fillNumbers.getFillNumbers()
        self.data.takeFillNumbers(fillnumber)
        for z in range(0, self.fillNumbers.getNumberOfFillNumbers()):  #1 +1
            path = self.basic_path + "/%d/%d_%s.txt" %(fillnumber[z], fillnumber[z], self.nameFileEnd)  #/group/online/tfc/ROOT/RunParameters/%d_Mu.txt
            print path
            d=np.loadtxt(path, delimiter=' ',dtype=[
                ('time_year', 'int'), ('time_month', 'int'), ('time_day', 'int'), ('time_hour', 'int'),
                ('time_minute', 'int'), ('time_sec', 'int'), ('value', 'float')]).T
            self.data.load(path, d)



