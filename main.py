import logging
from CustomHandlers import MongoHandler
import socket
from Messages import Message
import json
from logging.config import dictConfig
from logging_config import LOGGING_CONFIG

# Variables
hostname = socket.gethostname()
internal_ip = socket.gethostbyname(socket.gethostname())

dictConfig(LOGGING_CONFIG)

# Configs
logging.raiseExceptions = False

# Main logger - mongo and console
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

# Internal logger - console
internal_logger = logging.getLogger('intermal-mongo-logger')
internal_logger.setLevel(logging.DEBUG)
stream_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler()
handler.setFormatter(stream_formatter)
internal_logger.addHandler(handler)

# Send logs
msg = "Another message"
payload = Message(machine=22,
                  snif=2,
                  success=False,
                  host=hostname,
                  internal_ip=internal_ip)

my_logger.info(msg, extra=payload.as_dict())
