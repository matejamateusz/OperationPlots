__author__ = 'mmateja'

from LoadLumi import LoadLumi
from LoadMu import LoadMu
class LoadFiles():

    def __init__(self, name, fillNumbers):


         if 'lumi' in name:
            self.files=LoadLumi(fillNumbers)
            self.files.load()
         elif 'mu' in name:
            self.files=LoadMu(fillNumbers)
            self.files.load()
         elif 'pileup' in name:
             pass
         else:
             raise IOError("WRONG PATH")

    def getLoadedFiles(self):
        return  self.files