'''
Created on 31 janv. 2019

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
    
    import ImageXOR as IMIX
    import WifCombos as WIFC
    import LoadTools as TOOLS
    
except ImportError:
    print('You need to import tkinter and PIL')
    time.sleep(5)
    raise SystemExit

root=tk.Tk()
root.title("Crypto GUI")
root.geometry("1600x1600")

class CheckOpenWindow():
    def OpenXorWin(self):
    #def OpenXorWin(self,root):
        #IMIX.Xoring().XorWin(root)
        IMIX.Xoring().XorWin()
        """
        checkFrames = []
        for val,key in root.children.items():
            if isinstance(key,tk.Frame):                           
                checkFrames.append(str(key))
        
        if not(any("xoring" in x for x in checkFrames)):
            IMIX.Xoring().XorWin(root)
        """
        
    def OpenWifWin(self):
        WIFC.Combinations().WifCombosWin()
        
def LoadX(toolNum):
    TOOLS.LoadTools().RunX(toolNum)
    
def LoadI(toolNum):
    def switch(item):
        if item==0: CheckOpenWindow().OpenXorWin()
        elif item==1: CheckOpenWindow().OpenWifWin()
        
    switch(toolNum)
    
#add buttons in main frame
buttonExit = ttk.Button(root, text="Exit", command=lambda: sys.exit())
buttonExit.grid(sticky='E',row=1,column=0)

#Initializing tabs in root frame
tab_control = ttk.Notebook(root)

tabChecklist = ttk.Frame(tab_control)
tab_control.add(tabChecklist, text='Checklist', padding='1', state='normal')

tabAlphabets = ttk.Frame(tab_control)
tab_control.add(tabAlphabets, text='Alphabets', padding='1', state='normal')

tabRef = ttk.Frame(tab_control)
tab_control.add(tabRef, text='References', padding='1', state='hidden')

tabTools = ttk.Frame(tab_control)
tab_control.add(tabTools, text='Tools', padding='1', state='normal')

tabScripts = ttk.Frame(tab_control)
tab_control.add(tabScripts, text='Scripts', padding='1', state='normal')

tabAbout = ttk.Frame(tab_control)
tab_control.add(tabAbout, text='About', padding='1', state='normal')

tab_control.grid(sticky='N',row=0,column=0)

#############################################################################
#Add a series of buttons for external tools
NoXTools=12
XTool=[[] for k in range(0,NoXTools)]
LabelXTool=[[] for k in range(0,NoXTools)]
NameXTool=[[] for k in range(0,NoXTools)]
DescriptionXTool=[[] for k in range(0,NoXTools)]
for iterNumX in range(0,NoXTools):
    NameXTool[iterNumX]=StringVar()
    DescriptionXTool[iterNumX]=StringVar()
    
    XTool[iterNumX]=ttk.Button(tabTools,textvariable=NameXTool[iterNumX],command=lambda iterNumX=iterNumX:LoadX(iterNumX)).grid(sticky='NSEW',row=iterNumX+2,column=4)
    LabelXTool[iterNumX]=ttk.Label(tabTools,textvariable=DescriptionXTool[iterNumX]).grid(sticky='NSEW',row=iterNumX+2,column=5)

NameXTool[0].set("Color Pix")
NameXTool[1].set("Hash Knife")
NameXTool[2].set("Image to CSV")
NameXTool[3].set("Midi Editor 1")
NameXTool[4].set("Midi Editor 2")
NameXTool[5].set("Nonogram solver")
NameXTool[6].set("OCR Reader")
NameXTool[7].set("OpenPuff")
NameXTool[8].set("PNG Analyser")
NameXTool[9].set("Steganabara")
NameXTool[10].set("Stegsolve")
NameXTool[11].set("Threatstego")
#NameXTool[12].set("X-Ripper")

DescriptionXTool[0].set("Desktop screen pixel viewer")
DescriptionXTool[1].set("Hash cracking tool")
DescriptionXTool[2].set("Image to CSV / CSV to Image transformation tool upto 1000x1000 images")
DescriptionXTool[3].set("View tracks of midi type file")
DescriptionXTool[4].set("View music sheet of midi type file (with piano playing)")
DescriptionXTool[5].set("Black and white nonogram solver")
DescriptionXTool[6].set("Line and character extractor from images")
DescriptionXTool[7].set("Steganography tool")
DescriptionXTool[8].set("View chunks, validate image size, validate CRC chunks (PNG files only)")
DescriptionXTool[9].set("Image analysis tool")
DescriptionXTool[10].set("Image analysis tool")
DescriptionXTool[11].set("Steganography tool")
#DescriptionXTool[12].set("Search files and libraries for imbedded file types")
##################################################################################

#############################################################################
#Add a series of buttons for internal tools
NoITools=1
ITool=[[] for k in range(0,NoITools)]
LabelITool=[[] for k in range(0,NoITools)]
NameITool=[[] for k in range(0,NoITools)]
DescriptionITool=[[] for k in range(0,NoITools)]
for iterNumI in range(0,NoITools):
    NameITool[iterNumI]=StringVar()
    DescriptionITool[iterNumI]=StringVar()
    
    ITool[iterNumI]=ttk.Button(tabTools,textvariable=NameITool[iterNumI],command=lambda iterNumI=iterNumI:LoadI(iterNumI)).grid(sticky='NSEW',row=iterNumI+2,column=1)
    LabelITool[iterNumI]=ttk.Label(tabTools,textvariable=DescriptionITool[iterNumI]).grid(sticky='NSEW',row=iterNumI+2,column=2)

NameITool[0].set("Image XOR")
#NameITool[1].set("WIF validation")

DescriptionITool[0].set("Applying logical gates on images")
#DescriptionITool[1].set("Finding public addresses from valid WIF addresses")

##################################################################################

#Header labels
ttk.Label(tabTools,font=40,text="Internal Tools").grid(sticky='NSEW',row=1,column=1)
ttk.Label(tabTools,font=40,text="External Tools").grid(sticky='NSEW',row=1,column=4)

#Setting widths / heights of cells in Tools tab
tabTools.grid_rowconfigure(0, minsize=10)
tabTools.grid_rowconfigure(1, minsize=40)

tabTools.grid_columnconfigure(0, minsize=50)
tabTools.grid_columnconfigure(1, minsize=200)
tabTools.grid_columnconfigure(3, minsize=50)
tabTools.grid_columnconfigure(4, minsize=200)


class InitCheckList:
    def __init__(self): 

        #initialize Treeview
        checktree = ttk.Treeview(tabChecklist,height=32,selectmode = "extended")
        
        for elements in list_of_lists:
            arr_temp=[elements[1],elements[2]]
            checktree.insert('', 'end', text=elements[0], values = arr_temp)
        
        checktree.item('', open = True)
        checktree.grid(sticky='N',row=1,column=1)

        checktree['columns'] = ('col1','col2')
        
        checktree.column('#0', width=200, anchor='w')
        checktree.heading('#0', text='Type of puzzle')
        
        checktree.column('col1', width=500, anchor='w')
        checktree.heading('col1', text='Description')
        
        checktree.column('col2', width=500, anchor='w')
        checktree.heading('col2', text='Reference')

class InitAlphabets:
    def __init__(self):
        
        #initialize Treeview
        alphatree = ttk.Treeview(tabAlphabets,height=32, selectmode = "extended")
    
        for alphabet in range(0,len(list_of_Alphabets)):
            alphatree.insert('', 'end', text=list_of_Alphabets[alphabet], values = alphabet)
        
        #No nodes in tree, so unnecessary
        #alphatree.item('', open = True)
        alphatree.grid(sticky='N',row=1,column=1)
        
        alphatree['columns'] = ('col1')
        
        alphatree.column('#0', width=300, anchor='w')
        alphatree.heading('#0', text='Language')
        
        alphatree.column('col1', width=50, anchor='w')
        alphatree.heading('col1', text='Language name')
        
        #Hide the columns following the first one
        alphatree["displaycolumns"]=()
        
        #Define result of clicking on line in alphatree
        def selectItem(a):
            curItem = alphatree.focus()
            contents = (alphatree.item(curItem))
            Line_data = contents['values']

            for data in Line_data:
                
                basewidth = 500
                
                load = Image.open('Alphabets/'+ str(list_of_Alphabets[Line_data[0]]))
                wpercent = (basewidth / float(load.size[0]))
                hsize = int((float(load.size[1])*float(wpercent)))
                load = load.resize((basewidth,hsize),PIL.Image.ANTIALIAS)
                
                render = ImageTk.PhotoImage(load)
                img = ttk.Label(tabAlphabets, image = render)
                img.image=render
                img.grid(sticky='N',row=1,column=2)
        
                #Set up image on unclick
        alphatree.bind('<ButtonRelease-1>', selectItem)

class InitScripts:
    def __init__(self):
        
        scripttree = ttk.Treeview(tabScripts)
        scripttree['columns'] = ('col1','col2')
        
        scripttree.column('#0', width=200, anchor='w')
        scripttree.heading('#0', text='Code type')
        
        scripttree.column('col1', width=500, anchor='w')
        scripttree.heading('col1', text='Name')
        
        scripttree.column('col2', width=500, anchor='w')
        scripttree.heading('col2', text='Description')
        
        for elements in list_of_scripts:
            arr_temp=[elements[1],elements[2]]
            scripttree.insert('', 'end', text=elements[0], values = arr_temp)
      
        scripttree.grid(sticky='W',row=1,column=1)
        
        def selectItem(a):
            curItem = scripttree.focus()
            contents = (scripttree.item(curItem))
            Line_data = contents['values']

            EmptyLine = ttk.Label(tabScripts)
            EmptyLine.grid(sticky="W",row=2,column=1)
            
            f = open("Scripts/"+Line_data[0]+".txt", "r", encoding="UTF8").read()

            T=tk.Text(tabScripts,width=154)
            T.insert(tk.END,f)
            
            T.grid(sticky="W",row=3, column=1)
        
        #show script on item selection release
        scripttree.bind('<ButtonRelease-1>', selectItem)

class InitAbout:
    def __init__(self):
        AboutLine1 = ttk.Label(tabAbout, text="CryptoGUI")
        AboutLine1.grid(sticky="W",row=2, column=0)
        AboutLine1.config(font=("Courier",30))
        
        AboutLine2 = ttk.Label(tabAbout, text="Created by Mapl3Sn0w")
        AboutLine2.grid(sticky="W",row=3, column=0)
        AboutLine2.config(font=("Courier",25))
        
        AboutLine3 = ttk.Label(tabAbout, text="v0.1",anchor='w')
        AboutLine3.grid(sticky="W",row=4, column=0)
        AboutLine3.config(font=("Courier",25))
        
        AboutLine4 = ttk.Label(tabAbout, text="Created on: 2018-12-01")
        AboutLine4.grid(sticky="W",row=5, column=0)
        AboutLine4.config(font=("Courier",25))
        
        AboutLine5 = ttk.Label(tabAbout, text="Last modified on: 2019-02-03")
        AboutLine5.grid(sticky="W",row=6, column=0)
        AboutLine5.config(font=("Courier",25))
        
        AboutLine6 = ttk.Label(tabAbout, text="")
        AboutLine6.grid(sticky="W",row=7, column=0)
        AboutLine6.config(font=("Courier",15))
        
        AboutLine7 = ttk.Label(tabAbout, text="If you can make a distribution of this for windows or linux, including extra files and directories, please contact me")
        AboutLine7.grid(sticky="W",row=8, column=0)
        AboutLine7.config(font=("Courier",10))

        AboutLine8 = ttk.Label(tabAbout, text="Email: mapl3Sn0w@gmail.com")
        AboutLine8.grid(sticky="W",row=9, column=0)
        AboutLine8.config(font=("Courier",10))

        AboutLine9 = ttk.Label(tabAbout, text="Twitter: @mapl3Sn0w")
        AboutLine9.grid(sticky="W",row=10, column=0)
        AboutLine9.config(font=("Courier",10))

list_of_lists = []
with open('Tables/Checklist.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        list_of_lists.append(inner_list)

list_of_Alphabets = []
for alphabet in os.listdir("./Alphabets/"):
    if alphabet.endswith(".png"):
        list_of_Alphabets.append(str(alphabet))

list_of_scripts = []
with open('Tables/Table_Scripts.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        list_of_scripts.append(inner_list)

call = InitCheckList()
call = InitAlphabets()
call = InitScripts()
call = InitAbout()

#Insert nothing below this line
root.mainloop()