
import os
from shutil import rmtree

# 1 Realizar limpieza de archivos temporales de windows.


def clearDirTemp():

    path_temp = "C:/Windows/Temp/"
    path_temp_win = "C:/Users/Elvis Vasquez/AppData/Local/Temp/"

    elemTemp = os.listdir(path_temp)
    elemTempWin = os.listdir(path_temp_win)

    print("Elementos a eliminar en Temp:", len(elemTemp))
    print("Elementos a eliminar en Temp Windows:", len(elemTempWin))

    # Recorre los elementos de la lista, que corresponde a los nombre de los archivos
    # Se agrega la ruta mas el nombre del archivo
    for lista in elemTemp:
        eliminar = path_temp+lista
        try:
            os.remove(eliminar)
        except:
            print("Error al eliminar el archivo")

    # Temp de Windows
    for lista2 in elemTempWin:
        eliminar2 = path_temp_win+lista2
        try:
            os.remove(eliminar2)
        except:
            print("Error al eliminar el archivo")


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
