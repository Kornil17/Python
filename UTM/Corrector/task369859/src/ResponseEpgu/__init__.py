from kafkin import *
from parse_json import *
from loguru import logger
import json

logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')
logger.debug('__init__')