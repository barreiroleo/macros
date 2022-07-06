import logging, sys

def loggerConfig():
    logging.basicConfig(
        level=logging.INFO,
        handlers=[
            logging.FileHandler("macros.log"),
            logging.StreamHandler(sys.stdout)
        ],
        format='[%(levelname)s %(asctime)s] %(filename)s:%(lineno)d: %(message)s',
        datefmt='%H:%M:%S',
    )

