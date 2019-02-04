
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
     
except ImportError:
    print('You need to import tkinter and PIL')
    time.sleep(5)
    raise SystemExit

import imageio
import matplotlib.image as mimg
import os

class Xoring(tk.Frame):
    def XorWin(self):
        topXor = tk.Toplevel(self)
        topXor.title("Applyinig logical gates on images (XOR, AND, OR)")
        topXor.geometry("800x160")
        
        #Set variable input, output path string & operation done text
        FolderInput = StringVar()
        FolderOutput = StringVar()
        XorRun = StringVar()
        self.GateChoice = tk.IntVar(0)
        
        def AskInput(self):
            #root.withdraw()
            folder_selected = filedialog.askdirectory()
            #root.deiconify()
            topXor.lift()
            folder_selected = folder_selected + "/"
            FolderInput.set(folder_selected)

        def AskOutput(self):
            #root.withdraw()
            folder_selected = filedialog.askdirectory()
            #root.deiconify()
            topXor.lift()          
            folder_selected = folder_selected + "/"
            FolderOutput.set(folder_selected)
        
        def RunStart(self):
            XorRun.set("Status: Operation not started...")
        
        def RunOn(self):
            XorRun.set("Status: Tool activated, please wait...")
            
        def RunFinish(self):
            XorRun.set("Status: Logical gate operation on images finished")
        
        def RunErrorIO(self):
            XorRun.set("Status: Input/Output path error")
           
        def RunErrorLoad(self):
            XorRun.set("Statut: Image load error")
            
        def RunErrorSave(self):
            XorRun.set("Statut: Image save error")
        
        def LoadXOR(XorType,IPath,OPath):    
            
            if (os.path.isdir(IPath)==False or os.path.isdir(OPath)==False):
                RunErrorIO(self)
            else:
                RunOn(self)
                img=[]
                for name in os.listdir(IPath):
                    if name.endswith(".png"):    
                            try:
                                img.append(imageio.imread(IPath + name))
                            except:
                                RunErrorLoad(self)
            
                NumImages=len(img)
                
                #0: XOR, 1: AND, 2: OR
                for i in range(0,NumImages-1):
                    for j in range(i+1,NumImages):
                        if(i!=j):
                            if XorType == 0:
                                Mix = img[i]^img[j]
                            elif XorType == 1 :
                                Mix = img[i]&img[j]
                            elif XorType == 2:
                                Mix = img[i]|img[j]
                            
                            try:
                                mimg.imsave(OPath + str(i) + '-' + str(j) + ".png", Mix)
                            except: 
                                RunErrorSave(self)
                                
                RunFinish(self)
        
        RunStart(self)
        
        #Buttons to load input/output folders, set label to empty
        buttonInput= ttk.Button(topXor, text="Select input path",command=lambda: [AskInput(self),RunStart(self)])
        buttonOutput= ttk.Button(topXor, text="Select output path",command=lambda: [AskOutput(self),RunStart(self)])
        
        #Input/output paths chosen
        #Text in front of input / output paths chosen
        SaveInput = ttk.Label(topXor, textvariable=FolderInput)
        SaveOutput = ttk.Label(topXor, textvariable=FolderOutput)
        SaveTextI = ttk.Label(topXor, text="INPUT PATH:")
        SaveTextO = ttk.Label(topXor, text="OUTPUT PATH:")
        
        rbXOR = ttk.Radiobutton(topXor,text="XOR (default)",variable=self.GateChoice,value=0,command=lambda:RunStart(self))
        rbAND = ttk.Radiobutton(topXor,text="AND",variable=self.GateChoice,value=1,command=lambda:RunStart(self))
        rbOR = ttk.Radiobutton(topXor,text="OR",variable=self.GateChoice,value=2,command=lambda:RunStart(self))
        
        #Run tool with selected directories
        buttonRunXor = ttk.Button(topXor, text="Run tool",command=lambda: [RunStart(self),LoadXOR(self.GateChoice.get(),FolderInput.get(),FolderOutput.get())])
        
        #Variable label based on status of tool
        XorRunText = ttk.Label(topXor, textvariable=XorRun)
        #Exit button for topXor
        buttonExit = ttk.Button(topXor, text="Exit", command=lambda: topXor.destroy())
        
        #Setting default column widths for topXor
        topXor.grid_columnconfigure(1, minsize=100)
        topXor.grid_columnconfigure(2, minsize=100)
        topXor.grid_columnconfigure(3, minsize=400)
        
        #Placing widgets on topXor frame
        buttonInput.grid(sticky='NSEW',row=0,column=0)
        buttonOutput.grid(sticky='NSEW',row=1,column=0)
        SaveTextI.grid(sticky='E',row=0, column=1)
        SaveTextO.grid(sticky='E',row=1, column=1)
        SaveInput.grid(sticky='W',row=0, column=2)
        SaveOutput.grid(sticky='W',row=1, column=2)
        rbXOR.grid(sticky='NSEW',row=2,column=0)
        rbAND.grid(sticky='NSEW',row=3,column=0)
        rbOR.grid(sticky='NSEW',row=4,column=0)
        buttonRunXor.grid(sticky='NSEW',row=5,column=0)
        XorRunText.grid(sticky='NSEW',row=5, column=1,columnspan=3)
        buttonExit.grid(sticky='NSEW',row=5,column=4)