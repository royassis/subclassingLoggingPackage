import logging
import socket
from Messages import Message
from logging.config import dictConfig
import yaml


with open('logging_config.yaml', 'rt') as file:
    config = yaml.safe_load(file.read())
    dictConfig(config)

# Variables
hostname = socket.gethostname()
internal_ip = socket.gethostbyname(socket.gethostname())

# Configs
logging.raiseExceptions = False

# Main logger - mongo and console
my_logger = logging.getLogger('mongo-logger')

payload = Message(machine=22,
                  snif=2,
                  success=False,
                  host=hostname,
                  internal_ip=internal_ip)

my_logger.info("some info message", extra= payload.as_dict())
my_logger.error("some warning message", extra= payload.as_dict())

