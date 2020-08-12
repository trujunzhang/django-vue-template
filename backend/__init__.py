from os.path import abspath, dirname, exists, join
from os import makedirs
import logging
from backend import envs
import sys


def version():
    """
    get version from version file
    :return:
    """
    from backend import __version__
    return __version__.version()


loggers = {}


def get_logger(name=None, log_path=envs.LOG_PATH):
    """
    get logger by name and store it
    :param name:
    :return:
    """
    global loggers
    
    if not name:
        name = __name__
    
    if loggers.get(name):
        return loggers.get(name)
    
    # make log dir
    log_dir = dirname(log_path)
    if not exists(log_dir):
        makedirs(log_dir)
    
    logger = logging.getLogger(name)
    logger.setLevel(envs.LOG_LEVEL)
    
    # if log to console
    if envs.LOG_ENABLED and envs.LOG_TO_CONSOLE:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(level=envs.LOG_LEVEL)
        formatter = logging.Formatter(envs.LOG_FORMAT)
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)
    
    # if log to file
    if envs.LOG_ENABLED and envs.LOG_TO_FILE:
        # add file handler
        file_handler = logging.FileHandler(log_path, encoding='utf-8')
        file_handler.setLevel(level=envs.LOG_LEVEL)
        formatter = logging.Formatter(envs.LOG_FORMAT)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    # add to loggers
    loggers[name] = logger
    
    return logger
