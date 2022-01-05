import logging
import unittest
from pathlib import Path

from myhandlers import CustomRotatingFileHandler, CustomFileHandler


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
