LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'MongoHandler': {
            'level': 'INFO',
            'formatter': 'standard',
            'class':"CustomHandlers.MongoHandler",
            'host': 'localhost:27017:',
            'db': 'testdb',
            'collection': 'testcollection',
        }
    },
    'loggers': {
        'MongoLogger': {
            'handlers': ['MongoHandler'],
            'level': 'INFO',
            'propagate': False
        }
    }
}