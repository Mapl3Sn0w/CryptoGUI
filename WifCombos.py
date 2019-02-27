'''
Created on 4 févr. 2019

@author: Mapl3Sn0w
'''

#Proper way to validate cell contents
'''
import re

def validate(possible_new_value):
    if re.match(r'^[0-9a-fA-F]*$', possible_new_value):
        return True
    return False

entry = tk.Entry(root, validate="key", 
                 validatecommand=(root.register(validate), '%P'))
'''



#Proper way to allow copy-paste-cut
'''
def paste(self):
self.entry.event_generate('<Control-v>')
def cut(self):
self.entry.event_generate('<Control-x>')
def copy(self):
self.entry.event_generate('<Control-c>')
'''


try:
    import tkinter as tk
    from tkinter import ttk
    
    from tkinter import filedialog
    from tkinter import font as tkfont
    from tkinter import StringVar
    
    import PIL
    from PIL import ImageTk, Image
    
    import os
    import sys
    import time 
    import hashlib
    import binascii
    import base58
    import ecdsa
    #from pycoin.key import key_from_text
    
    import LoadMessages as x
    SMS = x.Messages()
    
    import itertools

except ImportError:
    print('You need to import tkinter and PIL')
    time.sleep(5)
    raise SystemExit

class Combinations(tk.Frame):
    def WifCombosWin(self):
        
        topWifCombos = tk.Toplevel(self)
        topWifCombos.title("Validating WIF or finding public addresses from WIF")
        topWifCombos.geometry("1600x1600")
        
        #Type of WIF, 0: K,L... / 1: 5...
        self.WifType = tk.IntVar(0)        
        
        def ripemd160(x):
            d = hashlib.new('ripemd160')
            d.update(x)
            return d
        
        def character_check(EntryStr):
            if len(EntryStr.get())>0:
                if not(any(EntryStr.get()[-1] in x for x in bs58)):
                    EntryStr.set(EntryStr.get()[:-1])
             
        def BoxesCheck(self):
            if self.WifType.get() == 1:
                itemEntry[51].delete(0,tk.END)
                itemEntry[51].config(state='disabled')
            elif self.WifType.get() == 0:
                itemEntry[51].config(state='enabled')
        
            SMS.RunStart(wifRun)
            
        def LoadWif(self):
            
            for box in Section:
                box.set("")
            
            n=0
            for item in (fullList.get()).split(","):
                if self.WifType.get() == 1 and n<51:
                    Section[n].set(item)
                    n=n+1
                elif self.WifType.get() == 0 and n<52:
                    Section[n].set(item)
                    n=n+1
            
            SMS.RunListLoad(wifRun)
            
        def RunWifCheck(self):
            
            SMS.RunOn(wifRun)
            
            if self.WifType.get()==0: 
                lenCheck=52
            elif self.WifType.get()==1: 
                lenCheck=51
            
            OutputShow=[]
            for entries in range(lenCheck):
                OutputShow.append(Section[entries].get())
            fullList.set(','.join(OutputShow))

            S = []
            SubList = []
            for CStr in Section:
                for item in CStr.get():
                    SubList.append(str(item))
                
                S.append(SubList)
                SubList = []
            
            #if length 52, delete last empty list item
            if lenCheck==51:
                del S[51]
            
            finalList = list(itertools.product(*S))
            
            for strWIF in finalList:
                JoinedStrWIF = ''.join(map(str,strWIF))
                
                if len(JoinedStrWIF) != lenCheck:
                    #print("Not correct length" + " | " + JoinedStrWIF)
                    continue
                
                try:
                
                    Step1 = (binascii.hexlify(base58.b58decode(JoinedStrWIF))).upper()
                    Short1 = Step1[0:-8]
                    
                    StringShaX1 = (hashlib.sha256(binascii.unhexlify(Short1)).hexdigest()).upper()
                    StringShaX2 = (hashlib.sha256(binascii.unhexlify(StringShaX1)).hexdigest()).upper()
                    
                    CheckSum1 = Step1[-8:].decode()
                    CheckSum2 = StringShaX2[0:8]
                    
                    if CheckSum1==CheckSum2:
                        #print("Valid WIF" + " | " + JoinedStrWIF)
                        ResultsBox.insert(tk.END, "Valid WIF" + JoinedStrWIF + '\n')
                    else:
                        pass
                        #print("WIF not valid" + " | " + JoinedStrWIF)
                    
                except:
                    pass
                    #print("Error in testing WIF" + " | " + JoinedStrWIF)
            
            SMS.RunFinish(wifRun)
            
        bs58 = ('1','2','3','4','5','6','7','8','9',
                 'A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z',
                 'a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        
        CharNum=[]
        fullList = StringVar()
        addString = StringVar()
        wifRun = StringVar()
        
        #Initialize status message
        SMS.RunStart(wifRun)
        
        itemLabel=[[] for _ in range(0,52)]
        itemEntry=[[] for _ in range(0,52)]
        Section=[[] for _ in range(0,52)]
        
        for iterNum in range(0,52):
            CharNum.append(iterNum)
            Section[iterNum]=StringVar()
        
        #For now i can't find a better way
        Section[0].trace("w", lambda *args: character_check(Section[0]))
        Section[1].trace("w", lambda *args: character_check(Section[1]))
        Section[2].trace("w", lambda *args: character_check(Section[2]))
        Section[3].trace("w", lambda *args: character_check(Section[3]))
        Section[4].trace("w", lambda *args: character_check(Section[4]))
        Section[5].trace("w", lambda *args: character_check(Section[5]))
        Section[6].trace("w", lambda *args: character_check(Section[6]))
        Section[7].trace("w", lambda *args: character_check(Section[7]))
        Section[8].trace("w", lambda *args: character_check(Section[8]))
        Section[9].trace("w", lambda *args: character_check(Section[9]))
        Section[10].trace("w", lambda *args: character_check(Section[10]))
        Section[11].trace("w", lambda *args: character_check(Section[11]))
        Section[12].trace("w", lambda *args: character_check(Section[12]))
        Section[13].trace("w", lambda *args: character_check(Section[13]))
        Section[14].trace("w", lambda *args: character_check(Section[14]))
        Section[15].trace("w", lambda *args: character_check(Section[15]))
        Section[16].trace("w", lambda *args: character_check(Section[16]))
        Section[17].trace("w", lambda *args: character_check(Section[17]))
        Section[18].trace("w", lambda *args: character_check(Section[18]))
        Section[19].trace("w", lambda *args: character_check(Section[19]))
        Section[20].trace("w", lambda *args: character_check(Section[20]))
        Section[21].trace("w", lambda *args: character_check(Section[21]))
        Section[22].trace("w", lambda *args: character_check(Section[22]))
        Section[23].trace("w", lambda *args: character_check(Section[23]))
        Section[24].trace("w", lambda *args: character_check(Section[24]))
        Section[25].trace("w", lambda *args: character_check(Section[25]))
        Section[26].trace("w", lambda *args: character_check(Section[26]))
        Section[27].trace("w", lambda *args: character_check(Section[27]))
        Section[28].trace("w", lambda *args: character_check(Section[28]))
        Section[29].trace("w", lambda *args: character_check(Section[29]))
        Section[30].trace("w", lambda *args: character_check(Section[30]))
        Section[31].trace("w", lambda *args: character_check(Section[31]))
        Section[32].trace("w", lambda *args: character_check(Section[32]))
        Section[33].trace("w", lambda *args: character_check(Section[33]))
        Section[34].trace("w", lambda *args: character_check(Section[34]))
        Section[35].trace("w", lambda *args: character_check(Section[35]))
        Section[36].trace("w", lambda *args: character_check(Section[36]))
        Section[37].trace("w", lambda *args: character_check(Section[37]))
        Section[38].trace("w", lambda *args: character_check(Section[38]))
        Section[39].trace("w", lambda *args: character_check(Section[39]))
        Section[40].trace("w", lambda *args: character_check(Section[40]))
        Section[41].trace("w", lambda *args: character_check(Section[41]))
        Section[42].trace("w", lambda *args: character_check(Section[42]))
        Section[43].trace("w", lambda *args: character_check(Section[43]))
        Section[44].trace("w", lambda *args: character_check(Section[44]))
        Section[45].trace("w", lambda *args: character_check(Section[45]))
        Section[46].trace("w", lambda *args: character_check(Section[46]))
        Section[47].trace("w", lambda *args: character_check(Section[47]))
        Section[48].trace("w", lambda *args: character_check(Section[48]))
        Section[49].trace("w", lambda *args: character_check(Section[49]))
        Section[50].trace("w", lambda *args: character_check(Section[50]))
        Section[51].trace("w", lambda *args: character_check(Section[51]))
        
        for itemNum in CharNum:
            #Widgets in topWifCombos Frame
            itemLabel[itemNum] = ttk.Label(topWifCombos, text=str(itemNum+1))        
            itemEntry[itemNum] = ttk.Entry(topWifCombos,textvariable=Section[itemNum])
            
            #Layout of labels and entry fields
            if itemNum < 26:
                itemLabel[itemNum].grid(sticky='NSEW',row=itemNum+3,column=2)
                itemEntry[itemNum].grid(sticky='NSEW',row=itemNum+3,column=3)
            else:
                itemLabel[itemNum].grid(sticky='NSEW',row=itemNum-26+3,column=5)
                itemEntry[itemNum].grid(sticky='NSEW',row=itemNum-26+3,column=6)
        
        #Top two entry boxes for full list and expected address
        fullEntry = ttk.Entry(topWifCombos,textvariable=fullList)
        addEntry = ttk.Entry(topWifCombos,textvariable=addString)
        
        #Add as option to check specific address in later version
        addEntry.config(state='disabled')
        #########################################################
        
        listLabel = ttk.Label(topWifCombos, text="WIF address characters:")
        addLabel = ttk.Label(topWifCombos, text="Check public address (optional):")
        
        #Radio buttons
        WifTypeLabel = ttk.Label(topWifCombos, text="Select the WIF type:")
        rbWif1 = ttk.Radiobutton(topWifCombos,text="Compressed(L/K)",variable=self.WifType,value=0,command=lambda:BoxesCheck(self)) #length 52
        rbWif2 = ttk.Radiobutton(topWifCombos,text="Uncompressed(5)",variable=self.WifType,value=1,command=lambda:BoxesCheck(self)) #length 51
        
        #Run button
        bttnRun = ttk.Button(topWifCombos,text="Check valid WIF addresses",command=lambda:RunWifCheck(self))
        
        #Load button
        lblComma = ttk.Label(topWifCombos, text="Use comma as a separator")
        bttnLoad = ttk.Button(topWifCombos,text="Load list",command=lambda:LoadWif(self))
        
        #Results label and textbox
        ResultsBox = tk.Text(topWifCombos)
        lblLoad = ttk.Label(topWifCombos,textvariable=wifRun)
        
        #Grid layout of widgets not defined with iteration
        fullEntry.grid(sticky='NSEW',row=0,column=1,columnspan=9)
        addEntry.grid(sticky='NSEW',row=1,column=1,columnspan=9)
        listLabel.grid(sticky='NSEW',row=0,column=0)
        addLabel.grid(sticky='NSEW',row=1,column=0)
        
        WifTypeLabel.grid(sticky='NSEW',row=3,column=0)
        rbWif1.grid(sticky='NSEW',row=4,column=0)
        rbWif2.grid(sticky='NSEW',row=5,column=0)
        bttnRun.grid(sticky='NSEW',row=7,column=0)
        bttnLoad.grid(sticky='NSEW',row=0,column=10)
        lblComma.grid(sticky='NSEW',row=0,column=11)
        
        ResultsBox.grid(sticky='NSEW',row=3,column=8,rowspan=52,columnspan=4)
        lblLoad.grid(sticky='NSEW',row=8,column=0)
        
        #Adjust layout of cells in frame
        topWifCombos.grid_columnconfigure(0, minsize=150)
        topWifCombos.grid_columnconfigure(1, minsize=40)
        topWifCombos.grid_columnconfigure(2, minsize=50)
        topWifCombos.grid_columnconfigure(3, minsize=100)
        topWifCombos.grid_columnconfigure(4, minsize=20)
        topWifCombos.grid_columnconfigure(5, minsize=50)
        topWifCombos.grid_columnconfigure(6, minsize=100)
        topWifCombos.grid_columnconfigure(7, minsize=50)
        topWifCombos.grid_columnconfigure(8, minsize=50)
        topWifCombos.grid_columnconfigure(9, minsize=100)
        topWifCombos.grid_columnconfigure(10, minsize=50)
        topWifCombos.grid_rowconfigure(2, minsize=20)
        topWifCombos.grid_rowconfigure(3, minsize=20)