import logging
import pymongo


class MongoHandler(logging.Handler):
    def __init__(self,host, db, collection, level=logging.DEBUG):
        super().__init__()
        self.host = host
        self.db = db
        self.collection = collection
        self.myclient= None
        self.internal_logger = logging.getLogger('internal-mongo-logger')

    def emit(self, record):
        try:
            with pymongo.MongoClient(f"mongodb://{self.host}/", serverSelectionTimeoutMS= 1000) as myclient:
                mycol = myclient[self.db][self.collection]
                # msg = self.format(record)
                mycol.insert_one(record.__dict__)
        except:
            self.handleError(record)

    def handleError(self, record):
        if logging.raiseExceptions:
            self.internal_logger.exception("Could not write to mongo")
        else:
            pass
