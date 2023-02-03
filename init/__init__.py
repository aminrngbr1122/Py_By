#Py-By Lib

class Py_By_start:
    """Py-By Class (:"""
    def Py_To_Exe(path, onefile = False, noconsole = False, path_icon = ''):
        """
        ## Use Py_By :
        ```
        from Py_By import Py_By_start
        \n
        pyby = Py_By_start()
        \n
        pyby.Py_To_Exe(path)
        ``` 
        """
        from os import system, getcwd, path
        import platform
        from sys import exit
        import clear
        system('-m pip install PyInstaller')
        clear.clear()
        try:
            import PyInstaller
        except:
            exit()
        c = []
        c.append('pyinstaller ')
        c.append(f'{path} ')
        if path.exists(path):
            if onefile == True:
                c.append('--onefile ')
            else:
                pass
            if noconsole == True:
                c.append('--noconsole ')
            else:
                pass
            if path.exists(path_icon):
                c.append(f'--icon={path_icon} ')
            else:
                pass
            m = ''.join(c)
            system(m)
            system(f'start {getcwd()}\dict')
            clear.clear()
        else:
            exit() 
        