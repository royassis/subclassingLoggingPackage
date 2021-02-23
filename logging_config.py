LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'with_host': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(host)s',
            'class':'CustomFormatters.ColoredFormatter'
        }
    },
    'handlers': {
        'MongoHandler': {
            'level': 'INFO',
            'formatter': 'standard',
            'class':"CustomHandlers.MongoHandler",
            'host': 'localhost:27017',
            'db': 'testdb',
            'collection': 'testcollection',
        },
        'BasicStreamHandler': {
            'level': 'INFO',
            'formatter': 'with_host',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        },
        'AnotherBasicStreamHandler': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        }
    },
    'loggers': {
        'mongo-logger': {
            'handlers': ['MongoHandler','BasicStreamHandler'],
            'level': 'INFO',
            'propagate':'True'
        },
        'internal-mongo-logger': {
            'handlers': ['AnotherBasicStreamHandler'],
            'level': 'INFO'
        }
    }
}