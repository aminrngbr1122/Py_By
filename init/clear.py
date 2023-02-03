import platform
from os import system

def clear():
    "Clear CMd Function Py-By"
    if platform.system().lower() == 'windows':
        system('cls')
    else:
        system('clear')