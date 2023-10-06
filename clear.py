

# 3 Eliminar historial de navegacion
import os
from shutil import rmtree


def clearDirTemp():
    # 1 Realizar limpieza de archivos temporales de windows.
    path_temp = "C:/Windows/Temp/"
    path_temp_win = "C:/Users/Elvis Vasquez/AppData/Local/Temp/"

    elemTemp = os.listdir(path_temp)
    elemTempWin = os.listdir(path_temp_win)

    print("Elementos a eliminar en Temp:", len(elemTemp))
    print("Elementos a eliminar en Temp Windows:", len(elemTempWin))

    #Recorre los elementos de la lista, que corresponde a los nombre de los archivos 
    #Se agrega la ruta mas el nombre del archivo
    for lista in elemTemp:
        eliminar=path_temp+lista
        try:
            os.remove(eliminar)
        except:
            print("Error al eliminar el archivo")

    #Temp de Windows
    for lista2 in elemTempWin:
        eliminar2=path_temp_win+lista2
        try:
            os.remove(eliminar2)
        except:
            print("Error al eliminar el archivo")
    
clearDirTemp()


