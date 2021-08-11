import logging
import logging.config
import logging.handlers


class LoggerConfig:

    server_conf = {
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
                'filename': "/tmp/app.log",
                'maxBytes': 1024 * 1024 * 50,
                'backupCount': 5,
            }
        },
        'loggers': {},
        'root': {
            'handlers': ['default'],
            'level': 'INFO',
        },
    }

    worker_conf = {
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
                'filename': "",
                'maxBytes': 1024 * 1024 * 50,
                'backupCount': 5,
            }
        },
        'loggers': {},
        'root': {
            'handlers': ['default'],
            'level': 'INFO',
        },
    }

    @classmethod
    def get_logger_conf(cls, process_type: str):
        logger_conf_dict = {"server": cls.server_conf, "worker": cls.worker_conf}
        if process_type not in logger_conf_dict:
            raise Exception(f"not found logger config:{process_type}")
        return logger_conf_dict.get(process_type)
