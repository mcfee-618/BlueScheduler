# coding=utf8

import os
import logging
import logging.config
import logging.handlers

from config import LOG_HOME

__all__ = ['init_log']

if not os.path.exists(LOG_HOME):
    os.mkdir(LOG_HOME)

# 文本日志
logger_file = os.path.join(LOG_HOME, 'project_control.log')

logging_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'hit': {
            'format': '%(asctime)s|%(message)s',
        },
        'detail': {
            'format': '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        },
    },
    'handlers': {
        'default': {
            '()': logging.handlers.RotatingFileHandler,
            'formatter': 'detail',
            'filename': logger_file,
            'maxBytes': 1024 * 1024 * 50,
            'backupCount': 5,
        }
    },
    'loggers': {
    },
    'root': {
        'handlers': ['default'],
        'level': 'INFO',
    },
}

_inited = False


def init_log():
    global _inited
    if not _inited:
        logging.config.dictConfig(logging_config)
        _inited = True


init_log()
