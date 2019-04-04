def RunStart(SV):
    SV.set("Status: Operation not started...")
    
def RunOn(SV):
    SV.set("Status: Tool activated, please wait...")
    
def RunFinish(SV):
    SV.set("Status: Operation finished")

def RunErrorIO(SV):
    SV.set("Status: Input/Output path error")

def RunErrorI(SV):
    SV.set("Status: Input path error")

def RunErrorO(SV):
    SV.set("Status: Output path error")

def RunErrorLoad(SV):
    SV.set("Status: Image load error")
    
def RunErrorSave(SV):
    SV.set("Status: Image save error")

def RunListLoad(SV):
    SV.set("Status: List loaded")
    
def RunOptionUnavailable(SV):
    SV.set("Status: Option unavailable at the moment")

def RunNotPNG(SV):
    SV.set("Status: Input file not in .png format")
    
def RunErrorIData(SV):
    SV.set("Status: Input data format incompatible")
##########################################################