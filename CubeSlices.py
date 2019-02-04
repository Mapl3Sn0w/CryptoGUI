#THIS FILE IS NOT OPERATIONAL YET

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
    
    import CubeSlices as Cube
     
except ImportError:
    print('You need to import tkinter and PIL')
    time.sleep(5)
    raise SystemExit

import matplotlib.pyplot as plt
import numpy as np
from numpy import empty

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

class CubeSlices(tk.Frame):
    def CS(self,root):
        topCube = tk.Toplevel(self)
        topCube.title("Cube visualization and cube slicing")
        topCube.geometry("800x200")
        
        
        RunCube = ttk.Button(topCube, text="Visualize cube",command=lambda: Cube.LoadCube(EntryBox.get()))
        RunSlices = ttk.Button(topCube, text="Visualize slices")
        EntryLabel = ttk.Label(topCube, text="Input cube matrix:")
        EntryBox = tk.Entry(topCube)
        
        #Layout of widgets
        EntryLabel.grid(sticky='NSEW',row=0, column=0)
        EntryBox.grid(sticky='NSEW',row=0, column=1)        
        RunCube.grid(sticky='NSEW',row=1, column=0)
        RunSlices.grid(sticky='NSEW',row=2, column=0)
        
        #Setting default column widths
        topCube.grid_columnconfigure(0, minsize=50)
        topCube.grid_columnconfigure(1, minsize=400)
        
def LoadSlices():
    pass

def LoadCube(Matrix):
        
    CubeMatrix = [[1,0,1],[1,0,1],[1,0,1]]
    
    CubeDimensions=3
        
    x=CubeDimensions
    y=CubeDimensions
    z=CubeDimensions
    
    # prepare some coordinates
    voxels=np.zeros([x, y, z], dtype=int)
    colors = np.empty(voxels.shape, dtype=object)
    
    # set the colors of each object
    for k in range(0,z):
        for j in range(0,y):
            for i in range(0,x):
                
    #HTML color makes cubes transparent like 
    #red and blue are: '#1f77b430' and '#ff000030'          
                if voxels[i][j][k]==1:
                    colors[i][j][k]='red'
                elif voxels[i][j][k]==-1:
                    colors[i][j][k]='blue'
    
    
    #plot all the cubes
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.voxels(voxels, facecolors=colors, edgecolor='k')
        
    plt.show()
    """
    #plotting by slice
    for plot in range(0,z):
        sliceL=np.squeeze(voxels[:,:,plot:plot+1],axis=2)
        sliceC=np.squeeze(colors[:,:,plot:plot+1],axis=2)
        
        plt.imshow(sliceL,cmap='hot')
        plt.savefig('Slice #' + str(plot) + '.png')
        plt.show()
    """