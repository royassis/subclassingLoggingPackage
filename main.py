import logging
from CustomHandlers import MongoHandler
import socket
from Messages import Message

hostname = socket.gethostname()
internal_ip = socket.gethostbyname(socket.gethostname())

logging.raiseExceptions = False

my_logger = logging.getLogger('mongo-logger')
my_logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(host)s')
stream_handler.setFormatter(stream_formatter)

mongo_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
mongo_handler = MongoHandler("localhost:27017", "testdb", "testcollection", logging.DEBUG)
mongo_handler.setFormatter(mongo_formatter)

my_logger.addHandler(stream_handler)
my_logger.addHandler(mongo_handler)

msg = "Another message"
payload = Message(machine=22,
                  snif=2,
                  success=False,
                  host=hostname,
                  internal_ip=internal_ip)

my_logger.info(msg, extra=payload.as_dict())
