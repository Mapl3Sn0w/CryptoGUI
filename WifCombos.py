'''
Created on 4 févr. 2019

@author: Mapl3Sn0w
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
         
    from pycoin.key import Key
    import itertools

except ImportError:
    print('You need to import tkinter and PIL')
    time.sleep(5)
    raise SystemExit

class Combinations(tk.Frame):
    def WifCombosWin(self):
        topWifCombos = tk.Toplevel(self)
        topWifCombos.title("Finding public addresses from valid WIF addresses")
        topWifCombos.geometry("1600x1600")
        
        self.WifType = tk.IntVar(0)        
        
        def BoxesCheck(self):
            if self.WifType.get() == 1:
                itemEntry[51].delete(0,tk.END)
                itemEntry[51].config(state='disabled')
            elif self.WifType.get() == 0:
                itemEntry[51].config(state='enabled')
        
        def RunWifCheck(self,WType):
            if WType==0: 
                lenCheck=52
            elif WType==1: 
                lenCheck=51
            
            OutputShow=[]
            for entries in range(lenCheck):
                OutputShow.append(Section[entries].get())
            fullList.set(OutputShow)
            
            S = []
            SubList = []
            for CStr in Section:
                for item in CStr.get():
                    SubList.append(item)
                S.append(SubList)
                SubList = []
            
            finalList = list(itertools.product(*S))
            
            for strWIF in finalList:
                JoinedStrWIF = ''.join(strWIF)
                
                if len(JoinedStrWIF) != lenCheck:
                    print("Not correct length" + " | " + JoinedStrWIF)
                    continue
                
                try:
                    pass
                except:
                    pass

        #For each value modified, modify the full string above
        vEntry=[]
            
        base58 = ('1','2','3','4','5','6','7','8','9',
                 'A','B','C','D','E','F','G','H','J','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z',
                 'a','b','c','d','e','f','g','h','i','j','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        
        CharNum=[]
        fullList = StringVar()
        addString = StringVar()
        itemLabel=[[] for k in range(0,52)]
        itemEntry=[[] for k in range(0,52)]
        Section=[[] for k in range(0,52)]
        for iterNum in range(0,52):
            CharNum.append(iterNum)
            Section[iterNum]=StringVar()
        
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
        
        listLabel = ttk.Label(topWifCombos, text="Complete list:")
        addLabel = ttk.Label(topWifCombos, text="Check for specific public address:")
        #Radio buttons
        WifTypeLabel = ttk.Label(topWifCombos, text="Select the WIF type:")
        rbWif1 = ttk.Radiobutton(topWifCombos,text="Compressed(L/K)",variable=self.WifType,value=0,command=lambda:BoxesCheck(self)) #length 52
        rbWif2 = ttk.Radiobutton(topWifCombos,text="Uncompressed(5)",variable=self.WifType,value=1,command=lambda:BoxesCheck(self)) #length 51
        
        #Run button
        bttnRun = ttk.Button(topWifCombos,text="Find addresses",command=lambda:RunWifCheck(self,self.WifType.get()))
        
        #Grid layout of widgets not defined with iteration
        fullEntry.grid(sticky='NSEW',row=0,column=1,columnspan=7)
        addEntry.grid(sticky='NSEW',row=1,column=1,columnspan=7)
        listLabel.grid(sticky='NSEW',row=0,column=0)
        addLabel.grid(sticky='NSEW',row=1,column=0)
        
        WifTypeLabel.grid(sticky='NSEW',row=3,column=0)
        rbWif1.grid(sticky='NSEW',row=4,column=0)
        rbWif2.grid(sticky='NSEW',row=5,column=0)
        bttnRun.grid(sticky='NSEW',row=7,column=0)
        
        #Adjust layout of cells in frame
        topWifCombos.grid_columnconfigure(0, minsize=150)
        topWifCombos.grid_columnconfigure(1, minsize=40)
        topWifCombos.grid_columnconfigure(2, minsize=50)
        topWifCombos.grid_columnconfigure(3, minsize=100)
        topWifCombos.grid_columnconfigure(4, minsize=20)
        topWifCombos.grid_columnconfigure(5, minsize=50)
        topWifCombos.grid_columnconfigure(6, minsize=100)
        topWifCombos.grid_columnconfigure(7, minsize=700)
        topWifCombos.grid_rowconfigure(2, minsize=20)