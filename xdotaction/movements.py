from time import sleep
from os import system
try:
    from .basic import getactivewindow, selectwindow
    from .logs import loggerConfig, logging
except ImportError:
    from basic import getactivewindow, selectwindow
    from logs import loggerConfig, logging

loggerConfig()

def resize_screenkey():
    logging.info("Resizing screenkey")
    system(f'xdotool windowsize $(xdotool selectwindow) 1280 50')
    logging.info("Resizing screenkey exit")

def raise_vim(vim_window=None):
    logging.info("Raising vim")
    if vim_window is None: vim_window = selectwindow()
    system(f'xdotool windowactivate --sync {vim_window}')
    system(f'xdotool getactivewindow windowsize --sync 1280 720')
    logging.info("Raising vim exit")

def toggle_rec(prev_win=getactivewindow()):
    logging.info("Toggle recording")
    regex, rec = "^OBS [0-9]+\.[0-9]+\.[0-9]+ \(linux\) - ", "ctrl+r"
    system(f'xdotool search --name "{regex}" windowactivate --sync key {rec}')
    system(f'xdotool windowactivate {prev_win}')
    sleep(0.5)
    logging.info("Toggle recording exit ")
