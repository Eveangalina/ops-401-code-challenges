#!/usr/bin/python3

# Import libraries
import logging

# Create the log object
log = logging.getLogger("my_logger")

# Configure my logging object
logging.basicConfig(filename='bruteforce.log', level=logging.INFO, format='%(asctime)s - %(levelname)s')

log.info("Hello, World") 
log.warning("THIS IS A WARNING!")
log.critical("THIS IS CRITICAL")

# Define a function
def do_something():
    log.debug("Doing something!")