import logging
from CustomHandlers import MongoHandler
import socket
from Messages import Message

hostname = socket.gethostname()
internal_ip = socket.gethostbyname(socket.gethostname())

logging.basicConfig(
            format='%(asctime)s %(levelname)s %(message)s - %(internal_ip)s - %(host)s',
            level=logging.INFO,
            datefmt='%m/%d/%Y %I:%M:%S %p'
            )

my_logger = logging.getLogger('mongo-logger')
my_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
mongo_handler = MongoHandler("localhost:27017", "testdb", "testcollection")
mongo_handler.setFormatter(formatter)
my_logger.addHandler(mongo_handler)

msg = "Another message"
payload = Message(machine= 2,
                  snif= 2,
                  success= True,
                  host= hostname,
                  internal_ip= internal_ip)

my_logger.info(msg, extra = payload.as_dict())
