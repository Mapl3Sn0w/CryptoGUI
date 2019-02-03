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
    import ImageXOR as IMIX
     
except ImportError:
    print('You need to import tkinter and PIL')
    time.sleep(5)
    raise SystemExit

import imageio
import matplotlib.image as mimg
import os

class Xoring(tk.Frame):
    def XorWin(self,root):
        topXor = tk.Toplevel(self)
        topXor.title("Applyinig logical gates on images (XOR, AND, OR)")
        topXor.geometry("800x140")
        
        #Set variable input, output path string & operation done text
        FolderInput = StringVar()
        FolderOutput = StringVar()
        XorRun = StringVar()
        
        def AskInput():
            root.withdraw()
            folder_selected = filedialog.askdirectory()
            root.deiconify()
            topXor.lift()
            folder_selected = folder_selected + "/"
            FolderInput.set(folder_selected)

        def AskOutput():
            root.withdraw()
            folder_selected = filedialog.askdirectory()
            root.deiconify()
            topXor.lift()          
            folder_selected = folder_selected + "/"
            FolderOutput.set(folder_selected)
        
        def RunStart():
            XorRun.set("Status: Operation not started...")
        
        def RunFinish():
            XorRun.set("Status: Logical gate operation on images finished")
        
        RunStart()
        
        #Buttons to load input/output folders, set label to empty
        buttonInput= ttk.Button(topXor, text="Select input path",command=lambda: [AskInput(),RunStart()])
        buttonOutput= ttk.Button(topXor, text="Select output path",command=lambda: [AskOutput(),RunStart()])
        
        #Input/output paths chosen
        #Text in front of input / output paths chosen
        SaveInput = ttk.Label(topXor, textvariable=FolderInput)
        SaveOutput = ttk.Label(topXor, textvariable=FolderOutput)
        SaveTextI = ttk.Label(topXor, text="INPUT PATH:")
        SaveTextO = ttk.Label(topXor, text="OUTPUT PATH:")
        
        #Run tool with selected directory, set label to empty at start and to finish at end
        buttonRunXor = ttk.Button(topXor, text="Run tool",command=lambda: [IMIX.LoadXOR(0,FolderInput.get(),FolderOutput.get()),RunStart()])
        buttonRunXor = ttk.Button(topXor, text="Run tool",command=lambda: RunFinish())
        
        XorRunText = ttk.Label(topXor, textvariable=XorRun)
        
        buttonExit = ttk.Button(topXor, text="Exit", command=lambda: topXor.destroy())
        
        #Placing widget on top frame
        buttonInput.grid(sticky='W',row=0,column=0)
        buttonOutput.grid(sticky='W',row=1,column=0)
        SaveTextI.grid(sticky="W",row=2, column=0)
        SaveTextO.grid(sticky="W",row=3, column=0)
        SaveInput.grid(sticky="W",row=2, column=1)
        SaveOutput.grid(sticky="W",row=3, column=1)
        buttonRunXor.grid(sticky='W',row=4,column=0)
        XorRunText.grid(sticky="W",row=5, column=0)
        buttonExit.place(x=700,y=100)
        
def LoadXOR(XorType,IPath,OPath):    
    
    img=[]
    for name in os.listdir(IPath):
        if name.endswith(".png"):    
                try:
                    img.append(imageio.imread(IPath + name))
                except:
                    print("Input path error")

    NumImages=len(img)
    
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
                    print("Output path error")
    
    