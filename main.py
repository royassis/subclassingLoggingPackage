import logging
import socket
from Messages import Message
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

payload = Message(machine=22,
                  snif=2,
                  success=False,
                  host=hostname,
                  internal_ip=internal_ip)

my_logger.info("message", extra= payload.as_dict())

