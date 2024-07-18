import logging, logging.config, os
from utility.color_palette import RESET, CYAN, BOLD_WHITE, YELLOW, BOLD_RED, INTENSITY_RED
from config.get import environment, home_direcotry

LOG_LEVEL: str = "DEBUG" # {0:NOTSET, 10:DEBUG, 20:INFO, 30:WARNING, 40:ERROR, 50:CRITICAL}

class ColoredFormatter(logging.Formatter):

    COLORS = {
        "DEBUG": CYAN,
        "INFO": BOLD_WHITE,
        "WARNING": YELLOW,
        "ERROR": BOLD_RED,
        "CRITICAL": INTENSITY_RED
    }

    RESET_COLOR = RESET


    def format(self, record):
        log_color = self.COLORS.get(record.levelname, '')
        log_msg = super().format(record)
        return f"{log_color}{log_msg}{self.RESET_COLOR}"


logging_config = {
    "version": 1, # mandatory field
    "formatters": {
        "basic": {
            "format": "%(levelname)s:    [%(asctime)s: %(filename)s > %(funcName)s() Line(%(lineno)d)] %(message)s"
        },
        "basic_colored": {
            "()": ColoredFormatter,
            "format": "%(levelname)s:    [%(asctime)s: %(filename)s > %(funcName)s() Line(%(lineno)d)] %(message)s"
        }
    },
    "handlers": {
        "console": {
            "formatter": "basic_colored",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr"
        }
    }
}

if environment == "local":
    logging_config.update({
        "loggers": {
            "uvicorn": {
                "handlers": ["console"],
                "level": LOG_LEVEL           
            },
            "App": {
                "handlers": ["console"],
                "level": LOG_LEVEL
            },
            "sqlalchemy.engine.Engine": {
                "handlers": ["console"],
                "level": LOG_LEVEL
            }
        }
    })
elif environment == "development":
    logging_config.update({
        "handlers": {
            "file": {
                "formatter": "basic",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "{}/logs/app.log".format(home_direcotry),
                "when": "h",
                "interval": 1,
                "backupCount": 24, # one day
                "encoding": "UTF-8",
                "utc": True
            }
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["file"],
                "level": LOG_LEVEL           
            },
            "App": {
                "handlers": ["file"],
                "level": LOG_LEVEL
            },
            "sqlalchemy.engine.Engine": {
                "handlers": ["file"],
                "level": LOG_LEVEL
            }
        }
    })
elif environment == "test":
    LOG_LEVEL = "INFO"

    logging_config.update({
        "handlers": {
            "file": {
                "formatter": "basic",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "{}/logs/app.log".format(home_direcotry),
                "when": "h",
                "interval": 4,
                "backupCount": 18, # 3 days
                "encoding": "UTF-8",
                "utc": True
            }
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["file"],
                "level": LOG_LEVEL           
            },
            "App": {
                "handlers": ["file"],
                "level": LOG_LEVEL
            },
            "sqlalchemy.engine.Engine": {
                "handlers": ["file"],
                "level": LOG_LEVEL
            }
        }
    })
else:
    LOG_LEVEL = "ERROR"

    logging_config.update({
        "handlers": {
            "file": {
                "formatter": "basic",
                "class": "logging.handlers.TimedRotatingFileHandler",
                "filename": "{}/logs/app.log".format(home_direcotry),
                "when": "h",
                "interval": 12,
                "backupCount": 14, # 7 days
                "encoding": "UTF-8",
                "utc": True
            }
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["file"],
                "level": LOG_LEVEL           
            },
            "App": {
                "handlers": ["file"],
                "level": LOG_LEVEL
            },
            "sqlalchemy.engine.Engine": {
                "handlers": ["file"],
                "level": LOG_LEVEL
            }
        }
    })

logging.config.dictConfig(config=logging_config)
logger = logging.getLogger("App")
