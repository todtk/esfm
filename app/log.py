# -*- coding: utf-8 -*-

import os
import logging
import pathlib
from time import strftime, gmtime, time
from logging.config import dictConfig


class Log:

    def __init__(self):

        self.get_folder()
        self.get_config()
        self.logger = logging.getLogger('app')

    def get_folder(self):
        pathlib.Path(os.path.join(os.getcwd(), 'logs')).mkdir(parents=True, exist_ok=True)

    def get_config(self):
        logging.config.dictConfig(
            {
                "version": 1,
                "disabled_existing_loggers": False,
                "formatters": {
                    "default": {
                        "format": "[%(asctime)s] %(levelname)-10s | %(func)-15s | %(message)s",
                        "datefmt": "%Y-%m-%d %H:%M:%S",
                    },
                    "extract": {
                        "format": "[%(asctime)s] | EXTRACTED | %(path)s",
                        "datefmt": "%Y-%m-%d %H:%M:%S",
                    },
                },
                "handlers": {
                    "console": {
                        "level": "INFO",
                        "class": "logging.StreamHandler",
                        "formatter": "default",
                    },
                    "debug": {
                        "level": "DEBUG",
                        "class": "logging.FileHandler",
                        "filename": f"logs/app.log",
                        "mode": "a",
                        "formatter": "default",
                    },
                    "info": {
                        "level": "INFO",
                        "class": "logging.FileHandler",
                        "filename": f"logs/{strftime('%d-%m-%Y', gmtime())}.log",
                        "mode": "a",
                        "formatter": "extract",
                    },
                },
                "loggers": {
                    "app": {
                        "handlers": ["console", "debug", "info"],
                        "level": "DEBUG",
                        "propagate": False,
                    },
                }
            }
        )

    def wrapper(self, mode: str = 'DEBUG'):

        levels = {
            'DEBUG': self.logger.debug,
            'INFO': self.logger.info,
            'WARNING': self.logger.warning,
            'ERROR': self.logger.error,
            'CRITICAL': self.logger.critical,
        }

        def __logger(function):

            sample = {
                'func': str(function.__qualname__).lower(),
                'file': None,
                'path': None,
            }

            def __function(*args, **kwargs):
                __result = function(*args, **kwargs)

                if mode == 'INFO':
                    if not __result:
                        return __result

                levels.get(mode)(
                    msg=__result,
                    extra={
                        **sample,
                        **kwargs
                    },
                )

                return __result
            return __function
        return __logger


log = Log()
