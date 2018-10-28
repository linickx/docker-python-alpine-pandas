#!/usr/bin/env python
# coding=utf-8
"""
    Simple Test Import
"""

import sys
import logging

logging.basicConfig(format='[%(levelname)s] %(asctime)s %(message)s', level=logging.DEBUG)
logger = logging.getLogger("test")

try:
    import pandas as pd
    logger.info("Pandas Works!")
except:
    logger.critical("Pandas Not installed")
    logger.debug("Exception: %s", sys.exc_info()[1])
    sys.exit(1)
