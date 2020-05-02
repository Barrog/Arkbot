import time
from random import choice
from ark_manager import *

from locks import Lock

import logging
from debug import setup_logging

log = logging.getLogger("ark_manager")
setup_logging()

import argparse
parser = argparse.ArgumentParser(description='Restart ark server.')
parser.add_argument("--message", dest='message', default=None, help="Message to add to broadcast, usually reason for restart.")
args = parser.parse_args()

if args.message:
    args.message = args.message.strip()
    if not args.message.endswith("."):
        args.message = args.message + ". "
    else:
        args.message = args.message + " "

lock = Lock()

if lock.locked:
    log.debug("Another script already running, exit...")
    sys.exit()

