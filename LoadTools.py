'''
Created on 5 févr. 2019

@author: Mapl3Sn0w
'''

import subprocess

class LoadTools:
    def RunX(self,toolNum):   

        def switch(item):
            if item==0: subprocess.call(['.\\XTools\\ColorPix.exe'])
            elif item==1: subprocess.call(['.\\XTools\\hash_knife.exe'])
            elif item==2: subprocess.call(['.\\XTools\\ImageToCSV.exe'])
            elif item==3: subprocess.call(['.\\XTools\\MidiEditor.exe'])
            elif item==4: subprocess.call(['.\\XTools\\MidiSheetMusic-2.6.exe'])
            elif item==5: subprocess.call(['java', '-jar', '.\\XTools\\bgusolver_gui_102.jar'])
            elif item==6: subprocess.call(['java', '-jar', '.\\XTools\\JavaOCR.jar'])
            elif item==7: subprocess.call(['.\\XTools\\OpenPuff.exe'])
            elif item==8: subprocess.call(['.\\XTools\\PNG_Analyzer.exe'])
            elif item==9: subprocess.call(['java', '-jar', '.\\XTools\\steganabara-1.1.1.jar'])
            elif item==10: subprocess.call(['java', '-jar', '.\\XTools\\Stegsolve.jar'])
            elif item==11: subprocess.call(['.\\XTools\\threatstego.exe'])
            #elif item==12:
            #    subprocess.call(['.\\XTools\\X-Ripper.exe','.\\XTools\\X-Ripper.ini'])
        
        switch(toolNum)
