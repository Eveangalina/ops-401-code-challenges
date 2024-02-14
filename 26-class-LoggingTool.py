#!/usr/bin/python3

# Script Name:                  Event Logging Tool p.1
# Author:                       E Campos
# Date of latest revision:      FEB2024
# Purpose:                      This script configures logging with a custom logger named "my_logger", sets up basic logging settings to write log messages to a file named "bruteforce.log", and logs informational, warning, and debug messages to the configured log file.

# Configure logging

import logging
import os


# Configure logging
log = logging.getLogger("my_logger")

# Configure object
logging.basicConfig(filename='bruteforce.log',level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

log.info("Hello, World")
log.warning("THIS IS A WARNING!")
# Define Function
def do_something():
    log.debug("Doing something!")