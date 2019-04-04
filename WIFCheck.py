import tkinter as tk
from tkinter import ttk

from tkinter import filedialog
from tkinter import StringVar

import os

#import external files########################################################
try:
    from LoadMessages import * 
    from FunctionsBTC import *
    from FunctionsMath import *

except ImportError:
    print('dependent file import error')
    raise SystemExit
##############################################################################

class Combinations(tk.Frame):
    def WifCombosWin(self):
        
        topWifCombos = tk.Toplevel(self)
        topWifCombos.title("Validating WIF or finding public addresses from WIF")
        topWifCombos.geometry("850x220")       
        
        wifRun = StringVar()
        WIFAddString = StringVar()
        ExAddString = StringVar()
        FileInput = StringVar()
        FolderOutput = StringVar()
        self.OptionalAddress = tk.IntVar(0)
        self.WIFOutputChoice = tk.IntVar(0)
        
        def character_check_Base58(EntryStr):
            if len(EntryStr.get())>0:
                if not(any(EntryStr.get()[-1] in x for x in bs58)):
                    EntryStr.set(EntryStr.get()[:-1])
    
            RunStart(wifRun)
        
        def WIFOptions1(self):
            if self.OptionalAddress.get()==0:
                ExpectedAdd.config(state='disabled')
                self.WIFOutputChoice.set(0)
                CBOutputAdd.config(state='enabled')
            elif self.OptionalAddress.get()==1:
                ExpectedAdd.config(state='enabled')
                CBOutputAdd.config(state='disabled')
        
        def AskInput(self):
            file_selected = filedialog.askopenfile()
            topWifCombos.lift()
            try:
                FileInput.set(file_selected.name)
            except:
                FileInput.set('')

        def AskOutput(self):
            folder_selected = filedialog.askdirectory()
            topWifCombos.lift()
            folder_selected = folder_selected + "/"
            FolderOutput.set(folder_selected)
                
        def RunWIFCheck(self):
            if (os.path.isfile(FileInput.get())==False or os.path.isdir(FolderOutput.get())==False):
                RunErrorIO(wifRun)
                    
            else:
                fw = open(FolderOutput.get() + 'output.txt','w')
        
                RunOn(wifRun)
                
                       
                with open(FileInput.get()) as fr:
                    lines = [line.rstrip('\n') for line in fr]
                
                if self.OptionalAddress.get() == 0:
                    #only loop once with or without address without checking condition for each WIF
                    if self.WIFOutputChoice.get() == 0:
                        for x in lines:               
                            if ValidateWIF(x) == True:
                                fw.write(x)
                                fw.write('\n')
                    elif self.WIFOutputChoice.get()==1:
                        for x in lines:               
                            if ValidateWIF(x) == True:
                                fw.write(x + ' | ' + WIFtoAddress(x))
                                fw.write('\n')
                #only output address if address found
                elif self.OptionalAddress.get() == 1:
                    for x in lines:               
                        if ValidateWIF(x) == True:
                            if WIFtoAddress(x)==ExAddString.get():
                                fw.write(x)
                                fw.write('\n')
                
                fw.close()
                RunFinish(wifRun)
            
        #Character validation trace
        WIFAddString.trace("w", lambda *args: character_check_Base58(WIFAddString))
        ExAddString.trace("w", lambda *args: character_check_Base58(ExAddString))
        
########FORMATING##############################################################################################################
########Separate frame for main section################################################################################
        InputFrame = tk.Frame(topWifCombos)
        InputFrame.grid(sticky='NSEW',row=0,column=0)
        
        #Input/Output labels 
        LoadTextI = ttk.Label(InputFrame, text="INPUT FILE:")
        SaveTextO = ttk.Label(InputFrame, text="OUTPUT PATH:")
        LoadI = ttk.Label(InputFrame, textvariable=FileInput,borderwidth=2, relief="solid")
        SaveO = ttk.Label(InputFrame, textvariable=FolderOutput,borderwidth=2, relief="solid")
       
        #Input/Output buttons
        buttonInput= ttk.Button(InputFrame, text="Select input path",command=lambda: [AskInput(self),RunStart(wifRun)])
        buttonOutput= ttk.Button(InputFrame, text="Select output path",command=lambda: [AskOutput(self),RunStart(wifRun)])
        
########FORMATING##############################################################################################################
########Separate frame for output section################################################################################
        OutputFrame = tk.Frame(topWifCombos)
        OutputFrame.grid(sticky='NSEW',row=1,column=0,pady=20)
        
        ExpectedAdd = ttk.Entry(OutputFrame,textvariable=ExAddString)
        CBExpectedAdd = ttk.Checkbutton(OutputFrame,text="Check a specific public address:",variable=self.OptionalAddress,command=lambda: [WIFOptions1(self),RunStart(wifRun)])
        CBOutputAdd = ttk.Checkbutton(OutputFrame,text="Output address corresponding to WIF",variable=self.WIFOutputChoice,command=lambda: RunStart(wifRun))
        bttnRun = ttk.Button(OutputFrame,text="Run Tool",command=lambda:RunWIFCheck(self))
       
        #Variable label based on status of tool
        WIFRunText = ttk.Label(OutputFrame, textvariable=wifRun)

####Layout-InputFrame################################################################      
        
        buttonInput.grid(sticky='NSEW',row=1,column=0)
        buttonOutput.grid(sticky='NSEW',row=2,column=0)
        LoadTextI.grid(sticky='E',row=1,column=1)
        SaveTextO.grid(sticky='E',row=2,column=1)
        LoadI.grid(sticky='NSEW',row=1,column=2,columnspan=5)
        SaveO.grid(sticky='NSEW',row=2,column=2,columnspan=5)

        #General cell configuration
        InputFrame.grid_columnconfigure(2,minsize=100)
        InputFrame.grid_columnconfigure(3,minsize=100)
        InputFrame.grid_columnconfigure(4,minsize=100)
        InputFrame.grid_columnconfigure(5,minsize=100)
        InputFrame.grid_columnconfigure(6,minsize=100)

######Layouy-OutputFrame##############################################################
        
        ExpectedAdd.grid(sticky='NSEW',row=0,column=2,columnspan=5)
        CBExpectedAdd.grid(sticky='NSEW',row=0,column=0)
        CBOutputAdd.grid(sticky='NSEW',row=1,column=0)
        
        bttnRun.grid(sticky='NSEW',row=2,column=0)
        WIFRunText.grid(sticky='NSEW',row=3,column=0,columnspan=7)
        
        #General cell configuration
        OutputFrame.grid_columnconfigure(2,minsize=100)
        OutputFrame.grid_columnconfigure(3,minsize=100)
        OutputFrame.grid_columnconfigure(4,minsize=100)
        OutputFrame.grid_columnconfigure(5,minsize=100)
        OutputFrame.grid_columnconfigure(6,minsize=100)

########Exit button #####################################################################
        buttonExit = ttk.Button(topWifCombos, text="Exit", command=lambda: topWifCombos.destroy())
        buttonExit.grid(sticky='NSEW',row=2,column=8)
        
########Initialize variables##################################################33
        RunStart(wifRun)
        WIFOptions1(self)