'''
Created on 13 nov. 2018

@author: Mapl3Sn0w
'''

try:
    from tkinter import ttk
    from tkinter import *
    from tkinter.ttk import *
    
    import PIL
    from PIL import ImageTk, Image
    
except ImportError:
    print('You need to import tkinter and PIL')
    raise SystemExit

#Initializing GUI
root=Tk()
root.title("Crypto GUI")
root.geometry("1600x1600")

#Initializing tabs in root frame
tab_control = ttk.Notebook(root)

tabChecklist = ttk.Frame(tab_control)
tab_control.add(tabChecklist, text='Checklist', padding='1', state='normal')

tabLanguages = ttk.Frame(tab_control)
tab_control.add(tabLanguages, text='Languages', padding='1', state='normal')

tabAlphabets = ttk.Frame(tab_control)
tab_control.add(tabAlphabets, text='Alphabets', padding='1', state='normal')

tabTables = ttk.Frame(tab_control)
tab_control.add(tabTables, text='Tables', padding='1', state='normal')

tabFunctions = ttk.Frame(tab_control)
tab_control.add(tabFunctions, text='Functions', padding='1', state='normal')

tabLogic = ttk.Frame(tab_control)
tab_control.add(tabLogic, text='Logic', padding='1', state='normal')

tabRef = ttk.Frame(tab_control)
tab_control.add(tabRef, text='References', padding='1', state='normal')

tabPrograms = ttk.Frame(tab_control)
tab_control.add(tabPrograms, text='Programs & scripts', padding='1', state='normal')

tabAbout = ttk.Frame(tab_control)
tab_control.add(tabAbout, text='About', padding='1', state='normal')

tab_control.pack(expand=1, fill='both')


class InitCheckList:
    def __init__(self):
        
        #initialize Treeview
        checktree = ttk.Treeview(tabChecklist,height=32,selectmode = "extended")
        
        for elements in list_of_lists:
            arr_temp=[elements[1],elements[2]]
            checktree.insert('', '0', text=elements[0], values = arr_temp)
        
        checktree.item('', open = True)
        checktree.grid(sticky='N',row=1,column=1)

        checktree['columns'] = ('col1','col2')
        
        checktree.column('#0', width=200, anchor='w')
        checktree.heading('#0', text='Type of puzzle')
        
        checktree.column('col1', width=500, anchor='w')
        checktree.heading('col1', text='Description')
        
        checktree.column('col2', width=500, anchor='w')
        checktree.heading('col2', text='Reference')

        
class InitTables:
    def __init__(self):
        
        #initialize Treeview
        tabletree = ttk.Treeview(tabTables)
        
        tabletree.item('', open = True)
        tabletree.pack()

        tabletree['columns'] = ('col1')
        
        tabletree.column('#0', width=200, anchor='w')
        tabletree.heading('#0', text='Table')
        
        tabletree.column('col1', width=500, anchor='w')
        tabletree.heading('col1', text='Description')

class InitAlphabets:
    def __init__(self):
        
        #initialize Treeview
        alphatree = ttk.Treeview(tabAlphabets,height=32, selectmode = "extended")
                
        for elements in list_of_Alphabets:
            arr_temp=[elements[1]]
            alphatree.insert('', '0', text=elements[0], values = arr_temp)
        
        #No nodes in tree, so unnecessary
        #alphatree.item('', open = True)
        alphatree.grid(sticky='N',row=1,column=1)
        
        basewidth = 500
        
        load = Image.open('Futurama(AL1).png')
        wpercent = (basewidth / float(load.size[0]))
        hsize = int((float(load.size[1])*float(wpercent)))
        load = load.resize((basewidth,hsize),PIL.Image.ANTIALIAS)
        
        render = ImageTk.PhotoImage(load)
        img = Label(tabAlphabets, image = render)
        img.image=render
        img.grid(sticky='N',row=1,column=2)
        
        alphatree['columns'] = ('col1')
        
        alphatree.column('#0', width=300, anchor='w')
        alphatree.heading('#0', text='Language')
        
        alphatree.column('col1', width=50, anchor='w')
        alphatree.heading('col1', text='Language name')
        
        def selectItem(a):
            curItem = alphatree.focus()
            contents = (alphatree.item(curItem))
            Line_data = contents['values']
            
            for data in Line_data:
                print(data)
                #Set up image on unclick
            
        alphatree.bind('<ButtonRelease-1>', selectItem)
        
class InitAbout:
    def __init__(self):
        AboutLine1 = Label(tabAbout, text="CryptoGUI")
        AboutLine1.grid(sticky="W",row=2, column=0)
        AboutLine1.config(font=("Courier",30))
        
        AboutLine2 = Label(tabAbout, text="Created by Mapl3Sn0w")
        AboutLine2.grid(sticky="W",row=3, column=0)
        AboutLine2.config(font=("Courier",25))
        
        AboutLine3 = Label(tabAbout, text="v0.1",anchor='w')
        AboutLine3.grid(sticky="W",row=4, column=0)
        AboutLine3.config(font=("Courier",25))
        
        AboutLine4 = Label(tabAbout, text="Created on: 2018-12-01")
        AboutLine4.grid(sticky="W",row=5, column=0)
        AboutLine4.config(font=("Courier",25))
        
        AboutLine5 = Label(tabAbout, text="Last modified on: 2018-12-01")
        AboutLine5.grid(sticky="W",row=6, column=0)
        AboutLine5.config(font=("Courier",25))
        
        AboutLine6 = Label(tabAbout, text="")
        AboutLine6.grid(sticky="W",row=7, column=0)
        AboutLine6.config(font=("Courier",15))
        
        AboutLine7 = Label(tabAbout, text="If you can make a distribution of this for windows or linux, including extra files and directories, please contact me")
        AboutLine7.grid(sticky="W",row=8, column=0)
        AboutLine7.config(font=("Courier",10))

        AboutLine8 = Label(tabAbout, text="Email: mapl3Sn0w@gmail.com")
        AboutLine8.grid(sticky="W",row=9, column=0)
        AboutLine8.config(font=("Courier",10))

        AboutLine9 = Label(tabAbout, text="Twitter: @mapl3Sn0w")
        AboutLine9.grid(sticky="W",row=10, column=0)
        AboutLine9.config(font=("Courier",10))

list_of_lists = []
with open('Checklist.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        list_of_lists.append(inner_list)

list_of_Alphabets = []
with open('Alphabets.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        list_of_Alphabets.append(inner_list)

list_of_tables = []
with open('Tables.txt') as f:
    for line in f:
        inner_list = [elt.strip() for elt in line.split(',')]
        list_of_tables.append(inner_list)

call = InitCheckList()
call = InitTables()
call = InitAbout()
call = InitAlphabets()

#Everything goes above this
root.mainloop()
