
from user import user 

class lock():
    def__init__(self, lockid, locationid, scuritylevel):

        self.lockid=lockid

        self.locatoinid=locatoinid

        self.securitylevel=scuritylevel

        self.status="locked"

    def getLockId(self):
       return self.lockid
    def getLocatoinId(self):

        return self.locationid

    def getSecurityLevel(self):

        return self.securitylevel


    def getStatus(self):
        return self.status

    def setStatus(self, status):

        self.status=status

   def__str__(self):

        return self.lockid + ' ' +self.status

