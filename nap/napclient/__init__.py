import logging
from nap.common.log import Log

logger = Log().get_loggerWithName("console")

def start_debugging():
    global logger
    logger.setLevel(logging.DEBUG)