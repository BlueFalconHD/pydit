import os

def width():
    size = os.get_terminal_size()
    width = size[0]
    return(width)
def height():
    size = os.get_terminal_size()
    height = size[1]
    return(height)