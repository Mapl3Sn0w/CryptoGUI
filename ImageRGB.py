'''
Created on 13 févr. 2019

@author: Mapl3Sn0w
'''


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
    
    from PIL import Image
 
except ImportError:
    print('You need to import tkinter and imageio')
    time.sleep(5)
    raise SystemExit

class ImageRGB(tk.Frame):
    def IndividualRGB(self):
        topRGB = tk.Toplevel(self)
        topRGB.title("Create individual images from RGB sets")
        topRGB.geometry("800x160")
    
        #Set variable input, output path string & operation done text
        FolderInput = StringVar()
        FolderOutput = StringVar()
        RGBRun = StringVar()

        def AskInput(self):
            folder_selected = filedialog.askdirectory()
            topRGB.lift()
            folder_selected = folder_selected + "/"
            FolderInput.set(folder_selected)

        def AskOutput(self):
            folder_selected = filedialog.askdirectory()
            topRGB.lift()          
            folder_selected = folder_selected + "/"
            FolderOutput.set(folder_selected)
            
        def LoadRGB(IPath,OPath):    
            
            if (os.path.isdir(IPath)==False or os.path.isdir(OPath)==False):
                SMS.RunErrorIO(RGBRun)
            else:
                SMS.RunOn(RGBRun)
                time.sleep(1)
                img=[]
                for name in os.listdir(IPath):
                    if name.endswith(".png"):    
                            try:
                                img.append(imageio.imread(IPath + name))
                            except:
                                SMS.RunErrorLoad(RGBRun)
            
                NumImages=len(img)
                
                '''            
                            try:
                                mimg.imsave(OPath + str(i) + '-' + str(j) + ".png", Mix)
                            except: 
                                SMS.RunErrorSave(RGBRun)
                
                '''
                             
                SMS.RunFinish(RGBRun)
        
        SMS.RunStart(RGBRun)

    
        #Buttons to load input/output folders, set label to empty
        buttonInput= ttk.Button(topRGB, text="Select input path",command=lambda: [AskInput(self),SMS.RunStart(RGBRun)])
        buttonOutput= ttk.Button(topRGB, text="Select output path",command=lambda: [AskOutput(self),SMS.RunStart(RGBRun)])
        
        #Input/output paths chosen
        #Text in front of input / output paths chosen
        SaveInput = ttk.Label(topRGB, textvariable=FolderInput)
        SaveOutput = ttk.Label(topRGB, textvariable=FolderOutput)
        SaveTextI = ttk.Label(topRGB, text="INPUT PATH:")
        SaveTextO = ttk.Label(topRGB, text="OUTPUT PATH:")
        
        #Run tool with selected directories
        buttonRunRGB = ttk.Button(topRGB, text="Run tool",command=lambda: [SMS.RunStart(RGBRun),LoadRGB(FolderInput.get(),FolderOutput.get())])
        
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
       
        buttonRunRGB.grid(sticky='NSEW',row=5,column=0)
        RGBRunText.grid(sticky='NSEW',row=5, column=1,columnspan=3)
        buttonExit.grid(sticky='NSEW',row=5,column=4)

'''
im = Image.open('test.png') #your image
im = im.convert('RGB')

width = im.size[0] #define W and H
height = im.size[1]

list_RGB = []

for x in range(width):
    for y in range(height):
        RGB = im.getpixel((x,y))
        
        if RGB not in list_RGB:
            list_RGB.append(RGB)
        

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
                i+=1
            else:
                pass
                #im_new[colors].putpixel((x,y),(255,255,255))
    
    Save_Filename = 'im_new' + str(list_RGB[colors]) + '.png'       
    print(Save_Filename)  
    im_new[colors].save(Save_Filename)
'''