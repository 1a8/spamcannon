import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

LOGCONF = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'file': {
            'format': '[{asctime}.{msecs:0<3.0f}] {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'validate': True
        },
        'console': {
            'format': '[{asctime}.{msecs:0<3.0f}] {message}',
            'style': '{',
            'datefmt': '%H:%M:%S',
            'validate': True
        },
    },

    'handlers': {
        'file': {
            'level': 'INFO',
            'formatter': 'file',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': ROOT / 'spam.log',
            'encoding': 'UTF-8',
            'maxBytes': 1000000,
            'backupCount': 3
        },
        'console': {
            'level': 'DEBUG',
            'formatter': 'console',
            'class': 'logging.StreamHandler',
        }
    },

    'loggers': {
        '': {
            'handlers': [
                'file',
                'console'
            ],
            'level': 'INFO',
            'propagate': False
        }
    }
}
