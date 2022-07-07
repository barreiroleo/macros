from time import sleep
from xdotaction.logs import loggerConfig, logging
from xdotaction.basic import getactivewindow, selectwindow
from xdotaction.movements import raise_vim, resize_screenkey, toggle_rec
from xdotaction.vim_actions import toggle_lang
from xdotaction.demos import demo_code_actions, demo_custom_dir, demo_autoload, demo_update

init_window = getactivewindow()
vim_window = selectwindow()

def run_demos():
    toggle_rec(vim_window)
    demo_code_actions(lang="en")
    toggle_lang()
    demo_code_actions(lang="es")
    toggle_lang()
    toggle_rec(vim_window)
    sleep(1)

    toggle_rec(vim_window)
    demo_custom_dir()
    toggle_rec(vim_window)
    sleep(1)

    toggle_rec(vim_window)
    demo_autoload()
    toggle_rec(vim_window)
    sleep(1)

    toggle_rec(vim_window)
    demo_update()
    toggle_rec(init_window)


def main():
    loggerConfig()
    logging.info("Starting demos")
    # resize_screenkey()
    raise_vim(vim_window)
    run_demos()

if __name__ == '__main__':
    main()
