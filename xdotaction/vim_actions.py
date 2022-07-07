from time import sleep
try:
    from .basic import key_press, Key
except ImportError:
    from basic import key_press, Key
    from movements import raise_vim

def code_action(opt:int):
    key_press(f"{Key.leader} c a {str(opt)} {Key.enter}", 200)
    sleep(0.5)

def close_buffer():
    key_press(f'{Key.colon} b d {Key.enter}')
    sleep(0.5)

def go_up():
    key_press(f"g g 0", 200)

def open_vim():
    key_press(f"v i m {Key.enter}", 200)

def toggle_comment():
    key_press(f"g c c", 200)

def toggle_explorer(update=False):
    key_press(f"ctrl+h", 200),
    if update: key_press("R W h j l", 200)
    sleep(0.2)

def toggle_lang():
    go_up()
    key_press(f"j", 200), toggle_comment()
    key_press(f"j", 200), toggle_comment()
    sleep(0.5)

# raise_vim()
