import logging
import socket
import unittest
from logging.config import dictConfig
from pathlib import Path

import yaml

from CustomHandlers import CustomRotatingFileHandler, CustomFileHandler
from Messages import Message


class TestCustomLoggers(unittest.TestCase):

    def test_CustomRotatingFileHandler(self):
        logger = logging.getLogger(__name__)
        root = Path("c:\\temp\otest_CustomRotatingFileHandlers")
        f_handler = CustomRotatingFileHandler(str(root.joinpath("file.log")), backupCount=10 ** 6)
        f_handler.setLevel(logging.ERROR)

        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)

        logger.addHandler(f_handler)

        for _ in range(10):
            logger.error('This is an error')

    def test_CustomFileHandler(self):
        logger = logging.getLogger(__name__)
        root = Path("c:\\temp\otest_CustomFileHandler")
        f_handler = CustomFileHandler(str(root), "file.log")
        f_handler.setLevel(logging.ERROR)

        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)

        logger.addHandler(f_handler)

        for _ in range(10):
            logger.error('This is an error')

    def test_MongoHandler(self):
        with open('logging_config_files/logging_config.yaml', 'rt') as file:
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

        my_logger.info("some info message", extra=payload.as_dict())
        my_logger.error("some warning message", extra=payload.as_dict())
