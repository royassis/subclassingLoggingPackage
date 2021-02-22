import logging
import pymongo

class MongoHandler(logging.Handler):
    def __init__(self,host, db, collection, level=logging.DEBUG):
        super().__init__()
        self.host = host
        self.db = db
        self.collection = collection
        self.myclient= None
        self.internal_logger = self.set_internal_logger(level)

    def set_internal_logger(self, level):
        internal_logger = logging.getLogger('intermal-mongo-logger')
        internal_logger.setLevel(level)
        stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(stream_formatter)
        internal_logger.addHandler(handler)
        return internal_logger

    def emit(self, record):
        try:
            myclient = pymongo.MongoClient(f"mongodb://{self.host}/", serverSelectionTimeoutMS= 1000)
            self.myclient = myclient
            mycol = myclient[self.db][self.collection]
            # msg = self.format(record)
            mycol.insert_one(record.__dict__)
            # myclient.close()
        except:
            self.handleError(record)

    def handleError(self, record):
        if logging.raiseExceptions:
            self.internal_logger.exception("Could not write to mongo")
        else:
            pass


    def close(self):
        try:
            self.myclient.close()
            self.internal_logger.debug("Closing connection of logger to MongoDB")
        except AttributeError:
            pass