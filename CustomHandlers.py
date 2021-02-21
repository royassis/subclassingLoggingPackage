import logging
import pymongo

class MongoHandler(logging.Handler):
    def __init__(self,host, db, collection ):
        super().__init__()
        self.host = host
        self.db = db
        self.collection = collection
        self.myclient= None

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
        if logging.raiseException:
            logging.exception("Could not write to mongo")
        else:
            pass


    def close(self):
        try:
            self.myclient.close()
            logging.info("Closing connection of logger to MongoDB")
        except AttributeError:
            pass