import os
import keyboard
import editor
from editor import start
import colorama
import os
import size
import time


def main():

    os.system("pip install -q keyboard")
    os.system("pip install -q colorama")

    os.system("cls")

    



    ########################

    '''
    mainscreen

    hayesEdit;
    __________________________________________________________________________________________________

                                            New File       Open
                                              (N)           (O)












    '''
    end = colorama.Style.RESET_ALL

    amt = size.width() - (2 + len("Pydit"))
    class mainScreen:
        header = " "*size.width() + "\n" + "  " + "  Pydit" + " "*(amt - 2) + "\n" + "_"*size.width()


    print(colorama.Back.LIGHTBLACK_EX + mainScreen.header + end)

    print("\n"*3)

    print("     New File       Open (WIP. Does not work.)\n     (N)            (O)\n     Tip: type :{help}: when editing a file for commands.")

    print("\n"*(size.height() - 13))


    while not keyboard.is_pressed('o') and not keyboard.is_pressed('n'):
        #nofunc
        nan = "lol"
        if nan == "lol":
            #nan
            nan = "nou"

    if keyboard.is_pressed('n') == True:
        os.system('cls')
        editor.start()

    if keyboard.is_pressed('o') == True:
        time.sleep(0.02)
        file = input('File? ')
        editor.openFile()

##########
main()