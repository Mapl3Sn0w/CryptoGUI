import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import StringVar
import os

from PIL import Image,ImageDraw,ImageFont
#import matplotlib.image as mimg

import numpy

#import string
from string import whitespace, punctuation, digits, ascii_uppercase, ascii_lowercase

#External file import#########################################################################
try:
    from LoadMessages import * 
    from FunctionsListsArraysTuples import *
    from FunctionsMath import *
 
except ImportError:
    print('dependent file import error')
    raise SystemExit
#############################################################################################

class Arecibo(tk.Frame):
    def AreciboTransformation(self):
        topAT = tk.Toplevel(self)
        topAT.title("Applying Arecibo style transformation for all combinations")
        topAT.geometry("600x280")
        
        #Set variable input, output path string & operation done text
        FileInput = StringVar()
        FolderOutput = StringVar()
        ATRun = StringVar()
        BaseXVar = StringVar()
        BaseXCharVar = StringVar()
        self.oWS = tk.IntVar(0)
        self.oP = tk.IntVar(0)
        self.oD = tk.IntVar(0)
        self.oU = tk.IntVar(0)
        self.oL = tk.IntVar(0)
        self.ExtractionType = tk.IntVar(0)
        
        basedigits = ['2','3','4']
        
        def BaseSelection(self):
            if self.ExtractionType.get() == 1:
                    BaseXEntry.delete(0,tk.END)
                    BaseXCharEntry.delete(0,tk.END)
                    BaseXEntry.config(state='disabled')
                    BaseXCharEntry.config(state='disabled')
            elif self.ExtractionType.get() == 0:
                    BaseXEntry.config(state='enabled')
                    BaseXCharEntry.config(state='enabled')
            
            RunStart(ATRun)
        
        def character_check_1(EntryStr):
            if len(EntryStr.get())>0:
                if not(any(EntryStr.get()[-1] in x for x in basedigits)):
                    EntryStr.set(EntryStr.get()[:-1])
                if len(EntryStr.get())>1:
                    EntryStr.set(EntryStr.get()[1:])
                    
                character_check_2(BaseXCharVar)

        def character_check_2(EntryStr):
            if len(EntryStr.get())>0:
                
                BaseLen = int(BaseXVar.get())
                
                if len(EntryStr.get())>BaseLen:
                    EntryStr.set(EntryStr.get()[:BaseLen])

                EntryStr.set(''.join(removedupes(EntryStr.get())))
            
        def AskInput(self):
            file_selected = filedialog.askopenfile()
            topAT.lift()
            try:
                FileInput.set(file_selected.name)
            except:
                FileInput.set('')

        def AskOutput(self):
            folder_selected = filedialog.askdirectory()
            topAT.lift()          
            folder_selected = folder_selected + "/"
            FolderOutput.set(folder_selected)
        
        def Exclusions(self):
            Ex = [self.oWS.get(),self.oP.get(),self.oD.get(),self.oU.get(),self.oL.get()]
            return Ex
        
        def Structured_image(s,W,H):
            new_imagearray=numpy.chararray((W, H))  
            x,y=0,0
            
            for position in range(len(s)):
                
                if position % W == 0 and position !=0:
                    y+=1
                    x=0
                elif position !=0:
                    x+=1
             
                new_imagearray[x][y]=s[position]
                
            return new_imagearray
        
        def Structured_string(s,W):
            new_string=''
            
            for position in range(len(s)):
                if position % W == 0 and position !=0:
                    new_string+='\n'
                    new_string+=s[position]
                else:
                    new_string+=s[position]
        
            return new_string
            
        def BaseXArt(String_factors,StringJoin,OPath):
            for BaseX_dimensions in String_factors:
                for orientation in range(2):
                    
                    x_dim = BaseX_dimensions[abs(0-orientation)]
                    y_dim = BaseX_dimensions[abs(1-orientation)]
                         
                    BaseColors = [(0,0,0),(255,255,255),(255,0,0),(255,255,0)]
                    
                    ColorScheme = int(BaseXVar.get())
                    
                    String_inclusions = list(BaseXCharVar.get())
                    
                    """
                    #Exclude characters not in selected characters for baseX
                    
                    StringList = list(StringJoin)
                    for position in range(len(StringList)):
                        if not(StringList[position] in String_inclusions):
                            StringList[position]=''
                    
                    StringJoin = ''.join(StringList)
                    """
                    
                    string_array = Structured_image(StringJoin,x_dim,y_dim)
                    
                    OColor = BaseColors[:ColorScheme]
                    
                    #save txt to png file
                    imgBaseX = Image.new('RGB', (x_dim, y_dim),(255,255,255))
                    
                    try:
                        for y in range(y_dim):
                            for x in range(x_dim):
                                OBaseX = String_inclusions.index(string_array[x][y].decode('UTF-8'))
                                imgBaseX.putpixel((x,y),OColor[OBaseX])
                    except:
                        imgBaseX.putpixel((x,y),(0,0,0))
                               
                    imgBaseX.save(OPath+'Test['+str(x_dim)+'-'+str(y_dim)+'].png')
                    
        def asciiArt(String_factors,StringJoin,OPath):
            for ascii_dimensions in String_factors:
                    for orientation in range(2):                       
                        x_dim = ascii_dimensions[abs(0-orientation)]
                        y_dim = ascii_dimensions[abs(1-orientation)]
                    
                        structured = Structured_string(StringJoin,x_dim)
                         
                        #save text to txt file
                        txt_save = open(OPath+'Test['+str(x_dim)+'-'+str(y_dim)+'].txt', "w")
                        txt_save.write(structured)
                        txt_save.close()
                               
                        img = Image.new('RGB', (36+7*x_dim, 36+16*y_dim),(255,255,255))
                        d = ImageDraw.Draw(img)
                        d.text((20, 20), structured, fill=(0, 0, 0))
                        
                        #save txt to png file
                        img.save(OPath+'Test['+str(x_dim)+'-'+str(y_dim)+'].png')
        
        def LoadAT(Exclusions,IFile,OPath):    
            if (os.path.isfile(IFile)==False or os.path.isdir(OPath)==False):
                RunErrorIO(ATRun)
            else:
                RunOn(ATRun)
                
                s=''
                with open (IFile, "r") as txtfile:
                    s=txtfile.read().replace('\n', '')
                
                String_factors = factors(len(s))
                
                Char_type = [whitespace,punctuation,digits,ascii_uppercase,ascii_lowercase]
                
                Char_exclusions = ''
                for _ in range(len(Exclusions)):
                    if Exclusions[_]==1:
                        Char_exclusions += Char_type[_]
                
                StringList = list(s)
                for position in range(len(StringList)):
                    if StringList[position] in Char_exclusions:
                        StringList[position]=''
                
                StringJoin = ''.join(StringList)
                
                if self.ExtractionType.get()==0:
                    #BaseX option
                    call = BaseXArt(String_factors,StringJoin,OPath)
                
                elif self.ExtractionType.get()==1:
                    #Ascii art option
                    call = asciiArt(String_factors, StringJoin, OPath)
                
                RunFinish(ATRun)
        
        RunStart(ATRun)
        
        BaseXVar.trace("w", lambda *args: character_check_1(BaseXVar))
        BaseXCharVar.trace("w", lambda *args: character_check_2(BaseXCharVar))
        
#FORMATING##############################################################################################################

        #Buttons to load input/output folders, set label to empty
        buttonInput= ttk.Button(topAT, text="Select input file",command=lambda: [AskInput(self),RunStart(ATRun)])
        buttonOutput= ttk.Button(topAT, text="Select output path",command=lambda: [AskOutput(self),RunStart(ATRun)])
        
        #Input/output paths chosen
        #Text in front of input / output paths chosen
        SaveInput = ttk.Label(topAT, textvariable=FileInput)
        SaveOutput = ttk.Label(topAT, textvariable=FolderOutput)
        SaveTextI = ttk.Label(topAT, text="INPUT PATH:")
        SaveTextO = ttk.Label(topAT, text="OUTPUT PATH:")
        
        #Exclude the following types of characters:
        ExclusionText = ttk.Label(topAT, text="Exclude the following types of characters:")
        cbWS = ttk.Checkbutton(topAT, text="Whitespace", variable=self.oWS,command=lambda:RunStart(ATRun))
        cbP = ttk.Checkbutton(topAT, text="Punctuation", variable=self.oP,command=lambda:RunStart(ATRun))
        cbD = ttk.Checkbutton(topAT, text="Digits", variable=self.oD,command=lambda:RunStart(ATRun))
        cbU = ttk.Checkbutton(topAT, text="Uppercase", variable=self.oU,command=lambda:RunStart(ATRun))
        cbL = ttk.Checkbutton(topAT, text="Lowercase", variable=self.oL,command=lambda:RunStart(ATRun))
        
        #Type of extraction
        ExtractionTypeText = ttk.Label(topAT, text="Pick the extraction type:")
        rbBaseX = ttk.Radiobutton(topAT,text="Base X",variable=self.ExtractionType,value=0,command=lambda:[RunStart(ATRun),BaseSelection(self)])
        rbAsciiArt = ttk.Radiobutton(topAT,text="Ascii Art",variable=self.ExtractionType,value=1,command=lambda:[RunStart(ATRun),BaseSelection(self)])
        BaseXEntry = ttk.Entry(topAT,textvariable=BaseXVar)
        BaseXCharEntry = ttk.Entry(topAT,textvariable=BaseXCharVar)
        BaseXText = ttk.Label(topAT, text="Base (2,3 or 4):")
        BaseXCharText = ttk.Label(topAT, text="Characters (no spaces):")
        
        #Run tool with selected directories
        buttonRunAT = ttk.Button(topAT, text="Run tool",command=lambda: [RunStart(ATRun),LoadAT(Exclusions(self),FileInput.get(),FolderOutput.get())])
        
        #Variable label based on status of tool
        ATRunText = ttk.Label(topAT, textvariable=ATRun)
        #Exit button for topXor
        buttonExit = ttk.Button(topAT, text="Exit", command=lambda: topAT.destroy())
        
        #Placing widgets on topXor frame
        buttonInput.grid(sticky='NSEW',row=0,column=0)
        buttonOutput.grid(sticky='NSEW',row=1,column=0)
        SaveTextI.grid(sticky='E',row=0, column=1)
        SaveTextO.grid(sticky='E',row=1, column=1)
        SaveInput.grid(sticky='W',row=0, column=2)
        SaveOutput.grid(sticky='W',row=1, column=2)
        
        ExclusionText.grid(sticky='NSEW',row=2,column=0)
        cbWS.grid(sticky='NSEW',row=3,column=0)
        cbP.grid(sticky='NSEW',row=4,column=0)
        cbD.grid(sticky='NSEW',row=5,column=0)
        cbU.grid(sticky='NSEW',row=6,column=0)
        cbL.grid(sticky='NSEW',row=7,column=0)
        
        ExtractionTypeText.grid(sticky='NSEW',row=8,column=0)
        BaseXText.grid(sticky='NSEW',row=8,column=1)
        BaseXCharText.grid(sticky='NSEW',row=8,column=2)
        rbBaseX.grid(sticky='NSEW',row=9,column=0)
        BaseXEntry.grid(sticky='NSEW',row=9,column=1)
        BaseXCharEntry.grid(sticky='NSEW',row=9,column=2)
        rbAsciiArt.grid(sticky='NSEW',row=10,column=0)

        buttonRunAT.grid(sticky='NSEW',row=11,column=0)
        ATRunText.grid(sticky='NSEW',row=11, column=1,columnspan=3)
        buttonExit.grid(sticky='NSEW',row=11,column=4)