# coding=utf8

import os
import logging
import logging.config
import logging.handlers

_inited = False


def init_log(logger_config):
    global _inited
    if not _inited:
        logging.config.dictConfig(logger_config)
        _inited = True


