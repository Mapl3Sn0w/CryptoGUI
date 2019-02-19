
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog
    #from tkinter import font as tkfont
    from tkinter import StringVar
    
    import os
    #import sys
    import time 
        
    import imageio
    import matplotlib.image as mimg

    import LoadMessages as x
    SMS = x.Messages()
 
except ImportError:
    print('You need to import tkinter and imageio')
    time.sleep(5)
    raise SystemExit

class Xoring(tk.Frame):
    def XorWin(self):
        topXor = tk.Toplevel(self)
        topXor.title("Applying logical gates on images (XOR, AND, OR)")
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
        
        def LoadXOR(XorType,IPath,OPath):    
            
            if (os.path.isdir(IPath)==False or os.path.isdir(OPath)==False):
                SMS.RunErrorIO(XorRun)
            else:
                SMS.RunOn(XorRun)
                time.sleep(1)
                img=[]
                for name in os.listdir(IPath):
                    if name.endswith(".png"):    
                            try:
                                img.append(imageio.imread(IPath + name))
                            except:
                                SMS.RunErrorLoad(XorRun)
            
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
                                SMS.RunErrorSave(XorRun)
                                
                SMS.RunFinish(XorRun)
        
        SMS.RunStart(XorRun)
        
        #Buttons to load input/output folders, set label to empty
        buttonInput= ttk.Button(topXor, text="Select input path",command=lambda: [AskInput(self),SMS.RunStart(XorRun)])
        buttonOutput= ttk.Button(topXor, text="Select output path",command=lambda: [AskOutput(self),SMS.RunStart(XorRun)])
        
        #Input/output paths chosen
        #Text in front of input / output paths chosen
        SaveInput = ttk.Label(topXor, textvariable=FolderInput)
        SaveOutput = ttk.Label(topXor, textvariable=FolderOutput)
        SaveTextI = ttk.Label(topXor, text="INPUT PATH:")
        SaveTextO = ttk.Label(topXor, text="OUTPUT PATH:")
        
        rbXOR = ttk.Radiobutton(topXor,text="XOR (default)",variable=self.GateChoice,value=0,command=lambda:SMS.RunStart(XorRun))
        rbAND = ttk.Radiobutton(topXor,text="AND",variable=self.GateChoice,value=1,command=lambda:SMS.RunStart(XorRun))
        rbOR = ttk.Radiobutton(topXor,text="OR",variable=self.GateChoice,value=2,command=lambda:SMS.RunStart(XorRun))
        
        #Run tool with selected directories
        buttonRunXor = ttk.Button(topXor, text="Run tool",command=lambda: [SMS.RunStart(XorRun),LoadXOR(self.GateChoice.get(),FolderInput.get(),FolderOutput.get())])
        
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