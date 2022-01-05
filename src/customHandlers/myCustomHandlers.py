import logging
import pymongo
from datetime import datetime
from logging import FileHandler
from pathlib import Path
from logging.handlers import RotatingFileHandler

from customHandlers.helpers import rename_logfiles


class MongoHandler(logging.Handler):
    def __init__(self,host, db, collection):
        super().__init__()
        self.host = host
        self.db = db
        self.collection = collection
        self.myclient= None
        self.internal_logger = logging.getLogger('internal-mongo-logger')

    def emit(self, record):
        try:
            #TODO: pool connection ?
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

        
class PerRunFileHandler(FileHandler):
    def __init__(self, dirname, strftime="%Y-%m-%dT%H:%M:%S"):
        dirname = Path(dirname)
        dirname.mkdir(parents=True, exist_ok=True)
        filename = datetime.now().strftime(strftime) + ".log"
        filepath = dirname.joinpath(filename)
        super().__init__(filepath, mode="a")


class CustomFileHandler(FileHandler):
    def __init__(self, dirname, filename):
        dirname = Path(dirname)
        dirname.mkdir(parents=True, exist_ok=True)
        filepath = dirname.joinpath(filename)
        filename = Path(filename)
        rename_logfiles(dirname, filename)
        super().__init__(filepath, mode="a")


class CustomRotatingFileHandler(RotatingFileHandler):
    def __init__(self, filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False):
        Path(filename).parent.mkdir(parents=True, exist_ok=True)
        super().__init__(filename, mode, maxBytes, backupCount, encoding, delay)
