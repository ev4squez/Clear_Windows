import os
import shutil
from subprocess import run
from pathlib import Path

# 1 Realizar limpieza de archivos temporales de windows.
# agregar los MB eliminados

home: str = str(Path('~').expanduser())


def clearDirTemp():

    pathTemp = "C:/Windows/Temp/"
    pathTempWin = home+"/AppData/Local/Temp/"

    processTemp = run(['du', '-sh', pathTemp], capture_output=True, text=True)
    processTempWin = run(['du', '-sh', pathTempWin],
                         capture_output=True, text=True)

    sizeTemp = processTemp.stdout.split()
    sizeTempWin = processTempWin.stdout.split()

    elemTemp = os.listdir(pathTemp)
    elemTempWin = os.listdir(pathTempWin)

    print("Elementos :", len(elemTemp), sizeTemp)
    print("Elementos :", len(elemTempWin), sizeTempWin)

    # Recorre los elementos de la lista, que corresponde a los nombre de los archivos
    # Se agrega la ruta mas el nombre del archivo

    with os.scandir(pathTemp) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathTemp, dir)
            print(dirDelete)

            try:
                shutil.rmtree(dirDelete)
                print("Directory removed successfully")
            except FileNotFoundError:
                print("Directory does not exist")
            except PermissionError:
                print("Permission denied")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    with os.scandir(pathTempWin) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathTempWin, dir)
            print(dirDelete)

            try:
                shutil.rmtree(dirDelete)
                print("Directory removed successfully")
            except FileNotFoundError:
                print("Directory does not exist")
            except PermissionError:
                print("Permission denied")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    countTemp = 0
    for lista in elemTemp:
        eliminar = os.path.join(pathTemp, lista)
        try:
            os.remove(eliminar)
        except:
            countTemp += 1

    # Temp de Windows
    contWinTemp = 0
    for lista2 in elemTempWin:
        eliminar2 = os.path.join(pathTempWin, lista2)
        try:
            os.remove(eliminar2)
        except:
            contWinTemp += 1

    print("No se eliminaron ", countTemp)
    print("No se eliminaron ", contWinTemp)


def clearDirUser():

    pathDoc = home+"/Documents"
    pathMusic = home+"/Music"
    pathImg = home+"/Pictures"
    pathVideo = home+"/Videos"
    pathDownload = home+"/Downloads"
    pathDesktop = home+"/Desktop"

    processDoc = run(['du', '-sh', pathDoc], capture_output=True, text=True)
    processMusic = run(['du', '-sh', pathMusic],
                       capture_output=True, text=True)
    processImg = run(['du', '-sh', pathImg], capture_output=True, text=True)
    processVideo = run(['du', '-sh', pathVideo],
                       capture_output=True, text=True)
    processDownload = run(['du', '-sh', pathDownload],
                          capture_output=True, text=True)
    processDesktop = run(['du', '-sh', pathDesktop],
                         capture_output=True, text=True)

    sizeDoc = processDoc.stdout.split()
    sizeMusic = processMusic.stdout.split()
    sizeImg = processImg.stdout.split()
    sizeVideo = processVideo.stdout.split()
    sizeDownload = processDownload.stdout.split()
    sizeDesktop = processDesktop.stdout.split()

    elemDoc = os.listdir(pathDoc)
    elemMusic = os.listdir(pathMusic)
    elemImg = os.listdir(pathImg)
    elemVideo = os.listdir(pathVideo)
    elemDownload = os.listdir(pathDownload)
    elemDesktop = os.listdir(pathDesktop)

    print("Elementos en Documentos: ", len(elemDoc), " ->", sizeDoc)
    print("Elementos en Musica: ", len(elemMusic), " ->", sizeMusic)
    print("Elementos en Imagenes: ", len(elemImg), " ->", sizeImg)
    print("Elementos en Video: ", len(elemVideo), " ->", sizeVideo)
    print("Elementos en Download: ", len(elemDownload), " ->", sizeDownload)
    print("Elementos en Desktop: ", len(elemDesktop), " ->", sizeDesktop)

    # Recorre los elementos de la lista, que corresponde a los nombre de los archivos
    # Se agrega la ruta mas el nombre del archivo

    with os.scandir(pathDoc) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathDoc, dir)
            print(dirDelete)

            try:
                shutil.rmtree(dirDelete)
                print("Directory removed successfully")
            except FileNotFoundError:
                print("Directory does not exist")
            except PermissionError:
                print("Permission denied")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    with os.scandir(pathMusic) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathMusic, dir)
            print(dirDelete)

            try:
                shutil.rmtree(dirDelete)
                print("Directory removed successfully")
            except FileNotFoundError:
                print("Directory does not exist")
            except PermissionError:
                print("Permission denied")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    with os.scandir(pathImg) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathImg, dir)
            print(dirDelete)

            try:
                shutil.rmtree(dirDelete)
                print("Directory removed successfully")
            except FileNotFoundError:
                print("Directory does not exist")
            except PermissionError:
                print("Permission denied")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    with os.scandir(pathVideo) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathVideo, dir)
            print(dirDelete)

            try:
                shutil.rmtree(dirDelete)
                print("Directory removed successfully")
            except FileNotFoundError:
                print("Directory does not exist")
            except PermissionError:
                print("Permission denied")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    with os.scandir(pathDownload) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathDownload, dir)
            print(dirDelete)

            try:
                shutil.rmtree(dirDelete)
                print("Directory removed successfully")
            except FileNotFoundError:
                print("Directory does not exist")
            except PermissionError:
                print("Permission denied")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    with os.scandir(pathDesktop) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathDesktop, dir)
            print(dirDelete)

            try:
                shutil.rmtree(dirDelete)
                print("Directory removed successfully")
            except FileNotFoundError:
                print("Directory does not exist")
            except PermissionError:
                print("Permission denied")
            except Exception as e:
                print(f"An error occurred: {str(e)}")

    countDoc = 0
    countMusic = 0
    countImg = 0
    countVideo = 0
    countDownload = 0
    countDesktop = 0

    for doc in elemDoc:
        eliminarDoc = os.path.join(pathDoc, doc)
        try:
            os.remove(eliminarDoc)
        except:
            countDoc += 1

    for music in elemMusic:
        eliminarMusic = os.path.join(pathMusic, music)
        try:
            os.remove(eliminarMusic)
        except:
            countMusic += 1

    for img in elemImg:
        eliminarImg = os.path.join(pathImg, img)
        try:
            os.remove(eliminarImg)
        except:
            countImg += 1

    for video in elemVideo:
        eliminarVideo = os.path.join(pathVideo, video)
        try:
            os.remove(eliminarVideo)
        except:
            countVideo += 1

    for down in elemDownload:
        eliminarDown = os.path.join(pathDownload, down)
        try:
            os.remove(eliminarDown)
        except:
            countDownload += 1
    for desk in elemDesktop:
        eliminarDesk = os.path.join(pathDesktop, desk)
        try:
            os.remove(eliminarDesk)
        except:
            countDesktop += 1

    print("Error", countDoc, sizeDoc)
    print("Error", countMusic, sizeMusic)
    print("Error", countImg, sizeImg)
    print("Error", countVideo, sizeVideo)
    print("Error", countDownload, sizeDownload)
    print("Error", countDesktop, sizeDesktop)


clearDirUser()
