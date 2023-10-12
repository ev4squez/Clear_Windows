import os
import shutil
from subprocess import run
from pathlib import Path

# 1 Realizar limpieza de archivos temporales de windows.
# agregar los MB eliminados

home: str = str(Path('~').expanduser())


def clearDirTemp():

    pathTemp = "C:/Windows/Temp/"
    pathTempWin = "C:/Users/usuario/AppData/Local/Temp/"

    elemTemp = os.listdir(pathTemp)
    elemTempWin = os.listdir(pathTempWin)

    print("Elementos :", len(elemTemp))
    print("Elementos :", len(elemTempWin))

    # Recorre los elementos de la lista, que correspond a los nombre de los archivos
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

    homeUser = "C:/Users/usuario/"

    countOne = 0
    countDoc = 0
    countDocume = 0
    countMusic = 0
    countImg = 0
    countVideo = 0
    countDownload = 0
    countDesktop = 0
    countDesktop_1 = 0

    # Recorre los elementos de la lista, que corresponde a los nombre de los archivos
    # Se agrega la ruta mas el nombre del archivo

    pathOne = homeUser+"OneDrive"
    if not os.path.exists(pathOne):
        print("No encontrado")
    else:
        elemOne = os.listdir(pathOne)
        with os.scandir(pathOne) as ficheros:
            subdirectorios = [
                fichero.name for fichero in ficheros if fichero.is_dir()]

            for dir in subdirectorios:
                dirDelete = os.path.join(pathOne, dir)
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

        for one in elemOne:
            eliminarOne = os.path.join(pathOne, one)
            try:
                os.remove(eliminarOne)
            except:
                countOne += 1

    pathDownload = homeUser+"Downloads"
    if not os.path.exists(pathDownload):
        print("No encontrado")
    else:
        elemDownload = os.listdir(pathDownload)
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

        for down in elemDownload:
            eliminarDown = os.path.join(pathDownload, down)
            try:
                os.remove(eliminarDown)
            except:
                countDownload += 1

    pathDoc = homeUser+"Documentos"
    if not os.path.exists(pathDoc):
        print("No encontrado")
    else:
        elemDoc = os.listdir(pathDoc)
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

        for doc in elemDoc:
            eliminarDoc = os.path.join(pathDoc, doc)
            try:
                os.remove(eliminarDoc)
            except:
                countDoc += 1

    pathDocume = homeUser+"Documents"
    if not os.path.exists(pathDocume):
        print("No encontrado")
    else:
        elemDocume = os.listdir(pathDocume)
        with os.scandir(pathDocume) as ficheros:
            subdirectorios = [
                fichero.name for fichero in ficheros if fichero.is_dir()]

            for dir in subdirectorios:
                dirDelete = os.path.join(pathDocume, dir)
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

        for doc in elemDocume:
            eliminarDoc = os.path.join(pathDocume, doc)
            try:
                os.remove(eliminarDoc)
            except:
                countDocume += 1

    pathDesktop = homeUser+"Escritorio"
    if not os.path.exists(pathDesktop):
        print("No encontrado")
    else:
        elemDesktop = os.listdir(pathDesktop)
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

        for desk in elemDesktop:
            eliminarDesk = os.path.join(pathDesktop, desk)
            try:
                os.remove(eliminarDesk)
            except:
                countDesktop += 1

    pathDesktop_1 = homeUser+"Desktop"
    if not os.path.exists(pathDesktop_1):
        print("No encontrado")
    else:
        elemDesktop = os.listdir(pathDesktop_1)
        with os.scandir(pathDesktop_1) as ficheros:
            subdirectorios = [
                fichero.name for fichero in ficheros if fichero.is_dir()]

            for dir in subdirectorios:
                dirDelete = os.path.join(pathDesktop_1, dir)
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

        for desk in elemDesktop:
            eliminarDesk = os.path.join(pathDesktop_1, desk)
            try:
                os.remove(eliminarDesk)
            except:
                countDesktop_1 += 1

    pathMusic = homeUser+"Music"
    if not os.path.exists(pathMusic):
        print("No encontrado")
    else:
        elemMusic = os.listdir(pathMusic)
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

        for music in elemMusic:
            eliminarMusic = os.path.join(pathMusic, music)
            try:
                os.remove(eliminarMusic)
            except:
                countMusic += 1

    pathImg = homeUser+"Pictures"
    if not os.path.exists(pathImg):
        print("No encontrado")
    else:
        elemImg = os.listdir(pathImg)
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

        for img in elemImg:
            eliminarImg = os.path.join(pathImg, img)
            try:
                os.remove(eliminarImg)
            except:
                countImg += 1

    pathVideo = homeUser+"Videos"
    if not os.path.exists(pathVideo):
        print("No encontrado")
    else:
        elemVideo = os.listdir(pathVideo)
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

        for video in elemVideo:
            eliminarVideo = os.path.join(pathVideo, video)
            try:
                os.remove(eliminarVideo)
            except:
                countVideo += 1

    print("Error", countDoc)
    print("Error", countMusic)
    print("Error", countImg)
    print("Error", countVideo)
    print("Error", countDownload)
    print("Error", countDesktop)
    print("Error", countOne)


def clearGoogleChrome():
    # se debe de eliminar el direccorio  User Data
    # \AppData\Local\Google\Chrome
    # antes se debe cerrar el proceso

    browserExe = "chrome.exe"
    os.system("taskkill /f /im "+browserExe)
    pathBrowser = "C:/Users/usuario/AppData/Local/Google/Chrome/User Data/"

    with os.scandir(pathBrowser) as ficheros:
        subdirectorios = [
            fichero.name for fichero in ficheros if fichero.is_dir()]

        for dir in subdirectorios:
            dirDelete = os.path.join(pathBrowser, dir)
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

    elemChrome = os.listdir(pathBrowser)

    countChrome = 0
    for lista in elemChrome:
        eliminar = os.path.join(pathBrowser, lista)
        try:
            os.remove(eliminar)
        except:
            countChrome += 1

    print("No se eliminaron ", countChrome)


def cleanmgr():
    appPath = "C:/Windows/System32/cleanmgr.exe"
    os.system(appPath)


clearDirTemp()
clearDirUser()
clearGoogleChrome()
clearGoogleChrome()
cleanmgr()
