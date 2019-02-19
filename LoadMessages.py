'''
Created on 12 févr. 2019

@author: Mapl3Sn0w
'''

class Messages():
    def RunStart(self, SV):
        SV.set("Status: Operation not started...")
        
    def RunOn(self, SV):
        SV.set("Status: Tool activated, please wait...")
        
    def RunFinish(self, SV):
        SV.set("Status: Operation finished")
    
    def RunErrorIO(self, SV):
        SV.set("Status: Input/Output path error")
       
    def RunErrorLoad(self, SV):
        SV.set("Status: Image load error")
        
    def RunErrorSave(self, SV):
        SV.set("Status: Image save error")

    def RunListLoad(self, SV):
        SV.set("Status: List loaded")
    ##########################################################