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
    from PIL import Image,ImageDraw,ImageFont
    import imageio
    import matplotlib.image as mimg
except: 
    print("PIL/imageio/matplotlib import error")
    raise SystemExit

try:
    import string
    from string import whitespace, punctuation, digits, ascii_uppercase, ascii_lowercase
except:
    print('string import error')
    raise SystemExit

try:
    import LoadMessages as X
    SMS = X.Messages()
 
except ImportError:
    print('dependent file import error')
    raise SystemExit

class Arecibo(tk.Frame):
    def AreciboTransformation(self):
        topAT = tk.Toplevel(self)
        topAT.title("Applying Arecibo style transformation for all combinations")
        topAT.geometry("800x200")
        
        #Set variable input, output path string & operation done text
        FileInput = StringVar()
        FolderOutput = StringVar()
        ATRun = StringVar()
        self.oWS = tk.IntVar(0)
        self.oP = tk.IntVar(0)
        self.oD = tk.IntVar(0)
        self.oU = tk.IntVar(0)
        self.oL = tk.IntVar(0)
        
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
            
        def factors(n):
            factors_list=[]
            for i in range(1, int(n**0.5)+1):
                if n % i == 0:
                    factors_list.append([i,n//i])
            return factors_list
        
        def Structured_string(s,W):
            new_string=''
            
            for position in range(len(s)):
                if position % W == 0 and position !=0:
                    new_string+='\n'
                    new_string+=s[position]
                else:
                    new_string+=s[position]
        
            return new_string
        
        def LoadAT(Exclusions,IFile,OPath):    
            if (os.path.isfile(IFile)==False or os.path.isdir(OPath)==False):
                SMS.RunErrorIO(ATRun)
            else:
                SMS.RunOn(ATRun)
                
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
              
                for ascii_dimensions in String_factors:
                        
                    structured = Structured_string(StringJoin,ascii_dimensions[0])
                    
                    img = Image.new('RGB', (ascii_dimensions[0]*60, ascii_dimensions[1]*40),(255,255,255))
                    d = ImageDraw.Draw(img)
                    d.text((20, 20), structured, fill=(0, 0, 0))
                    
                    #save text to txt file
                    txt_save = open(OPath+'Test['+str(ascii_dimensions[0])+'-'+str(ascii_dimensions[1])+'].txt', "w")
                    txt_save.write(structured)
                    txt_save.close()
                    
                    #save txt to png file
                    img.save(OPath+'Test['+str(ascii_dimensions[0])+'-'+str(ascii_dimensions[1])+'].png')
                
                SMS.RunFinish(ATRun)
        
        SMS.RunStart(ATRun)

#FORMATING##############################################################################################################

        #Buttons to load input/output folders, set label to empty
        buttonInput= ttk.Button(topAT, text="Select input file",command=lambda: [AskInput(self),SMS.RunStart(ATRun)])
        buttonOutput= ttk.Button(topAT, text="Select output path",command=lambda: [AskOutput(self),SMS.RunStart(ATRun)])
        
        #Input/output paths chosen
        #Text in front of input / output paths chosen
        SaveInput = ttk.Label(topAT, textvariable=FileInput)
        SaveOutput = ttk.Label(topAT, textvariable=FolderOutput)
        SaveTextI = ttk.Label(topAT, text="INPUT PATH:")
        SaveTextO = ttk.Label(topAT, text="OUTPUT PATH:")
        
        #Exclude the following types of characters:
        ExclusionText = ttk.Label(topAT, text="Exclude the following types of characters:")
        cbWS = ttk.Checkbutton(topAT, text="Whitespace", variable=self.oWS,command=lambda:SMS.RunStart(ATRun))
        cbP = ttk.Checkbutton(topAT, text="Punctuation", variable=self.oP,command=lambda:SMS.RunStart(ATRun))
        cbD = ttk.Checkbutton(topAT, text="Digits", variable=self.oD,command=lambda:SMS.RunStart(ATRun))
        cbU = ttk.Checkbutton(topAT, text="Uppercase", variable=self.oU,command=lambda:SMS.RunStart(ATRun))
        cbL = ttk.Checkbutton(topAT, text="Lowercase", variable=self.oL,command=lambda:SMS.RunStart(ATRun))
        
        #Run tool with selected directories
        buttonRunAT = ttk.Button(topAT, text="Run tool",command=lambda: [SMS.RunStart(ATRun),LoadAT(Exclusions(self),FileInput.get(),FolderOutput.get())])
        
        #Variable label based on status of tool
        ATRunText = ttk.Label(topAT, textvariable=ATRun)
        #Exit button for topXor
        buttonExit = ttk.Button(topAT, text="Exit", command=lambda: topAT.destroy())
        
        #Setting default column widths for topXor
        topAT.grid_columnconfigure(1, minsize=100)
        topAT.grid_columnconfigure(2, minsize=100)
        topAT.grid_columnconfigure(3, minsize=400)
        
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
        buttonRunAT.grid(sticky='NSEW',row=8,column=0)
        ATRunText.grid(sticky='NSEW',row=8, column=1,columnspan=3)
        buttonExit.grid(sticky='NSEW',row=8,column=4)