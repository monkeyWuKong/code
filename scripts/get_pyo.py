#compile py files under the path(dir) to '.pyo'
#
#and filter some you do not want to be compiled.
#
#backup the code before using.
#
import os
import commands

nameList = []

dir = './code_dir'

nameList = [] 

#get file list
def listDir(dirTemp):  
    global nameList  
    if not os.path.exists(dirTemp):  
        print "file or directory isn't exist"  
        return  
          
    if os.path.isfile(dirTemp):  
        nameList.append(dirTemp)  
        return  
          
    resultList = os.listdir(dirTemp)  
      
    for fileOrDir in resultList:  
        listDir(dirTemp + "/" +fileOrDir)  
          
    return nameList  


files = listDir(dir)  

for file in files:
    if file[-3:] != '.py':
        continue
    
    if 'settings.py' in file:
        continue
    
    if 'urls.py' in file:
        continue
    
    if '__init__.py' in file:
        continue
    
    if 'manage.py' in file:
        continue
    
    #create pyo
    cmd = 'python -O -m py_compile %s' % file
    (status, output) = commands.getstatusoutput(cmd)
    
    #create pyc
    cmd = 'python -m py_compile %s' % file
    (status, output) = commands.getstatusoutput(cmd)
    
    #delete source py
    cmd = 'rm -rf  %s' % file
    (status, output) = commands.getstatusoutput(cmd)