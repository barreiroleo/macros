from os import system, popen

class Key:
    colon       = "\'colon\'"
    enter       = "\'Return\'"
    escape      = "\'Escape\'"
    exclamation = "\'exclam\'"
    minus       = "\'KP_Subtract\'"
    space       = "\'space\'"
    tab         = "\'Tab\'"
    leader      = "\'space\'"

def getactivewindow():
    return popen("xdotool getactivewindow").read()

def selectwindow():
    return popen("xdotool selectwindow").read()

def key_press(key:str, delay:int=12):
    system(f'xdotool key --clearmodifiers --delay {delay} {key}')

