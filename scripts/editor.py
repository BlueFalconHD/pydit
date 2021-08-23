
import mainScreen
import colorama
import os
import keyboard
import time
import size

def openFile():
    nan = 'lol'

fulltxt = []
fnametemp = ""



filename = "New File - Rename: :{name}:"

def tick(first):
    global fnametemp

    os.system('cls')

    if first == True:
        fnametemp = filename

        
    def setName(name):
        fnametemp = name        
        
    currentLine = ""
    #Render Top

        
    end = colorama.Style.RESET_ALL

    amt = size.width() - (2 + len(fnametemp))

    class main:
        header = " "*size.width() + "\n" + "  " + fnametemp + " "*amt + "\n" + "_"*size.width()

    print(colorama.Back.LIGHTBLACK_EX + main.header + end)

    print('')

    ########

    for i in range(len(fulltxt)):
        print(" " + fulltxt[i], end="")
    currentLine = input(" ")

    if currentLine == ':{name}:':
        #test
        print(' New name: ', end='')
        name = input('')
        fnametemp = name
        amt = size.width() - (2 + len(filename))
        os.system('cls')

        tick(False)

    elif currentLine == ':{back}:':
        fulltxt.pop()
        tick(False)
    elif currentLine == ":{clear}:":
        fulltxt.clear()
        tick(False)
    elif currentLine == ":{save}:":
        name = fnametemp
        location = input(' Location: ')
        try:
            file = open(location + name, 'x')
            file.close()
        except:
            print(" File arleady exists. overwriting")
        filew = open(location + name, 'w')
        for i in range(len(fulltxt)):
            filew.write(fulltxt[i])
    elif currentLine == ":{help}:":
        print(":{back}: - move back a line.\n:{clear}: - clear the document\n:{save}: - saves the file\n:{name}: - set the name.")
        input("Press any key to continue...")
        tick(False)
    else:
        fulltxt.append(currentLine + "\n")
        os.system('cls')


def main():
    global filename
    global fnametemp
    import mainScreen, colorama, os
    import keyboard
    mainScreen.os.system("cls")
    import time
    '''
    New File (Change Name - Shift+Alt+C)
    _______________________________________________________________________________________

    {EDITOR GOES HERE}














    =========================================================================================
    '''

    fulltxt = []

    


    

    while True:
        tick(False)
        
        time.sleep(0.001)
        
        os.system('cls')

def start():
    tick(True)
    main()
