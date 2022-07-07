from time import sleep
try:
    from .vim_actions import go_up, code_action, toggle_explorer, close_buffer
    from .basic import key_press, Key
    from .logs import loggerConfig, logging
except ImportError:
    from vim_actions import go_up, code_action, toggle_explorer, close_buffer, toggle_lang
    from basic import key_press, Key
    from movements import raise_vim

def demo_code_actions(lang:str):
    logging.info(f"Runing demo: code action for {lang}")
    def go_misspell(lang):
        logging.info(f"Going to misspell")
        if lang == "en": key_press("6 j 3 w", 200), code_action(3)
        if lang == "es": key_press("1 0 j 3 w", 200), code_action(2)
    def go_false_positive(lang):
        logging.info(f"Going to false positive")
        if lang == "en": key_press("j 0", 200), code_action(2)
        if lang == "es": key_press("j 0", 200), code_action(2)
    def go_add_rules(lang):
        logging.info(f"Going to add rule")
        if lang == "en": key_press("j w", 200), code_action(3)
        if lang == "es": key_press("j 2 w", 200), code_action(3)
    go_up()
    go_misspell(lang)
    go_false_positive(lang)
    go_add_rules(lang)
    logging.info(f"Quit demo: code action for {lang}")

def demo_custom_dir():
    logging.info(f"Running demo: custom dir")
    toggle_explorer(update=True)
    for i in range(6):
        key_press(f"j {Key.tab}", 400)
    key_press("h h", 200)
    toggle_explorer()
    close_buffer()
    logging.info(f"Quit demo: custom dir")

def demo_update():
    logging.info(f"Running demo: update")
    # lua require("ltex_extra").reload()
    toggle_explorer(update=True)
    key_press("j j j", 200)
    for i in range(4):
        key_press("D y", 200), sleep(0.5)
    key_press("W h", 200)
    toggle_explorer()
    key_press(f"{Key.colon} l u a {Key.space} r e q {Key.up} {Key.enter}", 200)
    logging.info(f"Quit demo: update")

def demo_autoload():
    logging.info(f"Running demo: autoload")
    key_press(f"{Key.colon} q a {Key.exclamation} {Key.enter}", 400)
    key_press(f'l s {Key.space} {Key.minus} a {Key.enter}', 200)
    key_press(f'v i m {Key.enter}', 200)
    toggle_explorer()
    key_press(f'G l', 100)
    toggle_explorer()
    for i in range(11):
        sleep(1)
        logging.info(f"Waiting for ltex {i}")
    logging.info(f"Quit demo: autoload")

# raise_vim()
# demo_code_actions(lang="en")
# toggle_lang()
# demo_code_actions(lang="es")
# toggle_lang()
# sleep(0.6)
# demo_update()
