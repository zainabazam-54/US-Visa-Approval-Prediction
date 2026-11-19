from logger import logging
import sys
from exception import USvisaException
import sys

logging.info("Welcome to our custom log")

try:
    a=2/0
except Exception as e:
    raise USvisaException(e,sys)
