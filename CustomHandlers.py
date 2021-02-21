import logging
import pymongo

class MongoHandler(logging.Handler):
    def __init__(self,host, db, collection ):
        super().__init__()
        self.host = host
        self.db = db
        self.collection = collection

    def emit(self, record):
        try:
            myclient = pymongo.MongoClient(f"mongodb://{self.host}/", serverSelectionTimeoutMS= 1000)
            mycol = myclient[self.db][self.collection]
            # msg = self.format(record)
            mycol.insert_one(record.__dict__)
            myclient.close()
        except Exception as e:
            print('CRITICAL DB ERROR! Logging to database not possible!')
            print(e)

