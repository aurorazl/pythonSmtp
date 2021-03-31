
import logging
import os
from pathlib import Path
slogger = logging.getLogger('cvat.server')
BASE_DIR = str(Path(__file__).parents[2])
server_file = logging.FileHandler(filename='cvat_server.log')
slogger.handlers = [server_file]
print(slogger.handlers)
slogger.info(222)
