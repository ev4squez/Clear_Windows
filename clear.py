import os
from subprocess import run
from pathlib import Path

# 1 Realizar limpieza de archivos temporales de windows.
# agregar los MB eliminados 

def clearDirTemp():

    pathTemp = "C:/Windows/Temp/"
    pathTempWin = "C:/Users/Elvis Vasquez/AppData/Local/Temp/"
    
     
    processTemp = run(['du', '-sh', pathTemp], capture_output=True, text=True)
    processTempWin = run(['du', '-sh', pathTempWin], capture_output=True, text=True)

    sizeTemp = processTemp.stdout.split()
    sizeTempWin = processTempWin.stdout.split()

    elemTemp = os.listdir(pathTemp)
    elemTempWin = os.listdir(pathTempWin)

    print("Elementos :", len(elemTemp), sizeTemp)
    print("Elementos :", len(elemTempWin), sizeTempWin)

    # Recorre los elementos de la lista, que corresponde a los nombre de los archivos
    # Se agrega la ruta mas el nombre del archivo
    countTemp = 0
    for lista in elemTemp:
        eliminar = pathTemp+lista
        try:
            os.remove(eliminar)
        except:
            countTemp += 1
            
    # Temp de Windows
    contWinTemp = 0
    for lista2 in elemTempWin:
        eliminar2 = pathTempWin+lista2
        try:
            os.remove(eliminar2)
        except:
            contWinTemp += 1

    print("No se eliminaron ", countTemp)
    print("No se eliminaron ", contWinTemp)


clearDirTemp()

def clearDirUser():

    pathDoc = "C:/Windows/Temp/"
    pathMusic = "C:/Windows/Temp/"
    pathImg = "C:/Windows/Temp/"
    pathVideo = "C:/Windows/Temp/"
    pathDownload = "C:/Windows/Temp/"

    elemDoc = os.listdir(pathDoc)
    elemMusic = os.listdir(pathMusic)
    elemImg = os.listdir(pathImg)
    elemVideo = os.listdir(pathVideo)
    elemDownload = os.listdir(pathDownload)

    print("Documentos: ", len(elemDoc))
    print("Musica: ", len(elemMusic))
    print("Imagenes: ", len(elemImg))
    print("Video: ", len(elemVideo))
    print("Download: ", len(elemDownload))

    # Recorre los elementos de la lista, que corresponde a los nombre de los archivos
    # Se agrega la ruta mas el nombre del archivo
    for lista in elemDoc:
        eliminar = pathDoc+lista
        try:
            os.remove(eliminar)
        except:
            print("Error al eliminar el archivo")

    for lista in elemMusic:
        eliminar = pathMusic+lista
        try:
            os.remove(eliminar)
        except:
            print("Error al eliminar el archivo")

    for lista in elemImg:
        eliminar = pathImg+lista
        try:
            os.remove(eliminar)
        except:
            print("Error al eliminar el archivo")

    for lista in elemVideo:
        eliminar = pathVideo+lista
        try:
            os.remove(eliminar)
        except:
            print("Error al eliminar el archivo")

    for lista in elemDownload:
        eliminar = pathDownload+lista
        try:
            os.remove(eliminar)
        except:
            print("Error al eliminar el archivo")
