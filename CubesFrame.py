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
    import ImageXOR as IMIX
     
except ImportError:
    print('You need to import tkinter and PIL')
    time.sleep(5)
    raise SystemExit

import matplotlib.pyplot as plt
import numpy as np
from numpy import empty

# This import registers the 3D projection, but is otherwise unused.
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import



class Slicing(tk.Frame):
    def Cube(self,root):
        topCube = tk.Toplevel(self)
        topCube.title("Cube visualization and cube slicing")
        topCube.geometry("800x200")



def LoadSlices():
    pass

def LoadCube():
        
    CubeMatrix = [[0,1,0],[0,1,0], [0,1,0]]
    
    for CubeLength in CubeMatrix:
        CubeDimensions=CubeLength
        
    #x=CubeDimensions
    #y=CubeDimensions
    #z=CubeDimensions
    
    x=3
    y=3
    z=3
    
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
    
    #plotting by slice
    for plot in range(0,z):
        sliceL=np.squeeze(voxels[:,:,plot:plot+1],axis=2)
        sliceC=np.squeeze(colors[:,:,plot:plot+1],axis=2)
        
        plt.imshow(sliceL,cmap='hot')
        plt.savefig('Slice #' + str(plot) + '.png')
        plt.show()