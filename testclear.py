
import os
from subprocess import run
from pathlib import Path


def clearDirTemp():

    pathTemp = "C:/Windows/Temp/"

    process = run(['du', '-sh', pathTemp], capture_output=True, text=True)
    sizeTemp = process.stdout.split()

    elemTemp = os.listdir(pathTemp)

    print("Elementos :", len(elemTemp), sizeTemp)

    count=0
    for lista in elemTemp:
        eliminar = pathTemp+lista
        
        try:
            os.remove(eliminar)
        except:
            #print("Error -->", lista)
            count+=1    
    print("No se pueden eliminar = ",count)
    
    elemTempNew = len(os.listdir(pathTemp))
  
    print("Se eliminaron ", len(elemTemp) - elemTempNew)

clearDirTemp()