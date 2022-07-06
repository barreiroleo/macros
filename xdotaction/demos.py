try:
    from .vim_actions import go_up, code_action, toggle_explorer, close_buffer
    from .basic import key_press, Key
except ImportError:
    from vim_actions import go_up, code_action, toggle_explorer, close_buffer
    from basic import key_press, Key

def demo_code_actions(lang:str):
    def go_misspell(lang):
        if lang == "en": key_press("6 j 3 w", 200), code_action(3)
        if lang == "es": key_press("1 0 j 3 w", 200), code_action(2)
    def go_false_positive(lang):
        if lang == "en": key_press("j 0", 200), code_action(2)
        if lang == "es": key_press("j 0", 200), code_action(2)
    def go_add_rules(lang):
        if lang == "en": key_press("j w", 200), code_action(3)
        if lang == "es": key_press("j 2 w", 200), code_action(3)
    go_up()
    go_misspell(lang)
    go_false_positive(lang)
    go_add_rules(lang)

def demo_custom_dir():
    toggle_explorer()
    key_press("R h h j l", 200)
    for i in range(6):
        key_press(f"j {Key.tab}", 400)
    key_press("h h", 200)
    toggle_explorer()
    close_buffer()

def demo_update():
    pass

def demo_autoload():
    key_press(f"{Key.colon} q a {Key.exclamation} {Key.enter}", 400)
    key_press(f'l s {Key.space} {Key.minus} a {Key.enter}', 200)
    key_press(f'v i m {Key.enter}', 200)
    toggle_explorer()
    key_press(f'G l', 100)
    toggle_explorer()
