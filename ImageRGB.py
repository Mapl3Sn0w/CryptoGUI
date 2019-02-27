try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter import StringVar
except:
    print("tkinter import error")
    raise SystemExit
    
try:
    import os
except:
    print("os import error")
    raise SystemExit

try:
    import time
except:
    print("time import error")
    raise SystemExit

try:        
    from PIL import Image
    import imageio
    import matplotlib.image as mimg
except: 
    print("PIL/imageio/matplotlib import error")
    raise SystemExit
    
try:
    import LoadMessages as X
    SMS = X.Messages()
 
except ImportError:
    print('dependent file import error')
    raise SystemExit

class ImageRGB(tk.Frame):
    def IndividualRGB(self):
        topRGB = tk.Toplevel(self)
        topRGB.title("Creating individual images from RGB sets")
        topRGB.geometry("900x140")
    
        #Set variable input, output path string & operation done text
        FileInput = StringVar()
        FolderOutput = StringVar()
        RGBRun = StringVar()
        self.OType = tk.IntVar(0)
        
        def AskInput(self):
            file_selected = filedialog.askopenfile()
            topRGB.lift()
            try:
                FileInput.set(file_selected.name)
            except:
                FileInput.set('')

        def AskOutput(self):
            folder_selected = filedialog.askdirectory()
            topRGB.lift()          
            folder_selected = folder_selected + "/"
            FolderOutput.set(folder_selected)
            
        def OpenRGB(OType,IFile,OPath):    
            #OPENRGB #########################################################
            list_RGB = None
            im = None
            width = None
            height = None
            
            if (os.path.isfile(IFile)==False or os.path.isdir(OPath)==False):
                SMS.RunErrorIO(RGBRun)
            elif IFile.endswith(".png")==False:
                SMS.RunNotPNG(RGBRun)
            else:
                SMS.RunOn(RGBRun)
       
                try:
                    im = Image.open(IFile) #your image
                    im = im.convert('RGB')
                    
                    width = im.size[0] #define W and H
                    height = im.size[1]
                    
                    list_RGB = []
                    
                    for x in range(width):
                        for y in range(height):
                            RGB = im.getpixel((x,y))
                            
                            if RGB not in list_RGB:
                                list_RGB.append(RGB)
                except:
                    SMS.RunErrorLoad(RGBRun)
            
            LoadRGB(list_RGB,im,width,height,OType,OPath)
                             
        def LoadRGB(list_RGB,im,width,height,OType,OPath):
                #LOADRGB #################################################
                if OType==0:
                    SMS.RunOptionUnavailable(RGBRun)
                elif OType==1:
                    im_new=[]
                    for i in range(0,len(list_RGB)):
                        im_new.append(i)
                    
                    for colors in range(0,len(list_RGB)):    
                        im_new[colors] = Image.new('RGB',(width,height))
                        i=0
                        
                        for x in range(width):
                            for y in range(height):
                                
                                if im.getpixel((x,y))==list_RGB[colors]:
                                    im_new[colors].putpixel((x,y),list_RGB[colors])
                                else:
                                    pass
                                    #im_new[colors].putpixel((x,y),(255,255,255))
                            
                        #Save 1 file for each different color in hex or RGB
                        try:
                            mimg.imsave(OPath + '-'.join(map(str,list_RGB[colors])) + ".png", im_new[colors])
                        except: 
                            SMS.RunErrorSave(RGBRun)
                            break
                
                    SMS.RunFinish(RGBRun)
                ############################################################
                
        SMS.RunStart(RGBRun)


#FORMATING##############################################################################################################

        #Buttons to load input/output folders, set label to empty
        buttonInput= ttk.Button(topRGB, text="Select input file",command=lambda: [AskInput(self),SMS.RunStart(RGBRun)])
        buttonOutput= ttk.Button(topRGB, text="Select output path",command=lambda: [AskOutput(self),SMS.RunStart(RGBRun)])
        
        rbSingleColor = ttk.Radiobutton(topRGB,text="Export a single color",variable=self.OType,value=0,command=lambda:SMS.RunStart(RGBRun))
        rbAllColors = ttk.Radiobutton(topRGB,text="Export all colors",variable=self.OType,value=1,command=lambda:SMS.RunStart(RGBRun))
        
        #Input/output paths chosen
        #Text in front of input / output paths chosen
        SaveInput = ttk.Label(topRGB, textvariable=FileInput)
        SaveOutput = ttk.Label(topRGB, textvariable=FolderOutput)
        SaveTextI = ttk.Label(topRGB, text="INPUT FILE:")
        SaveTextO = ttk.Label(topRGB, text="OUTPUT PATH:")
        
        #Run tool with selected directories
        buttonRunRGB = ttk.Button(topRGB, text="Run tool",command=lambda: [SMS.RunStart(RGBRun),OpenRGB(self.OType.get(),FileInput.get(),FolderOutput.get())])
        
        #Variable label based on status of tool
        RGBRunText = ttk.Label(topRGB, textvariable=RGBRun)
        #Exit button for topRGB
        buttonExit = ttk.Button(topRGB, text="Exit", command=lambda: topRGB.destroy())
        
        #Setting default column widths for topRGB
        topRGB.grid_columnconfigure(1, minsize=100)
        topRGB.grid_columnconfigure(2, minsize=100)
        topRGB.grid_columnconfigure(3, minsize=400)
        
        #Placing widgets on topRGB frame
        buttonInput.grid(sticky='NSEW',row=0,column=0)
        buttonOutput.grid(sticky='NSEW',row=1,column=0)
        SaveTextI.grid(sticky='E',row=0, column=1)
        SaveTextO.grid(sticky='E',row=1, column=1)
        SaveInput.grid(sticky='W',row=0, column=2)
        SaveOutput.grid(sticky='W',row=1, column=2)
        rbSingleColor.grid(sticky='NSEW',row=2,column=0)
        rbAllColors.grid(sticky='NSEW',row=3,column=0)
       
        buttonRunRGB.grid(sticky='NSEW',row=5,column=0)
        RGBRunText.grid(sticky='NSEW',row=5, column=1,columnspan=3)
        buttonExit.grid(sticky='NSEW',row=5,column=4)