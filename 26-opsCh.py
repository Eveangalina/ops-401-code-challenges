#!/usr/bin/python3

# Script Name:                  Event Logging Tool p.1
# Author:                       E Campos
# Date of latest revision:      FEB2024
# Purpose:                      The purpose of this script is to integrate logging into an existing Python tool to record events, facilitate debugging, and provide actionable information to support security operations and automated systems.
# Resources:                    


import logging
from logging.handlers import RotatingFileHandler

# Function to configure logging
def setup_logging():
    # Create a custom logger
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.DEBUG)  # Set to the lowest level to capture all types of logs

    # Create handlers
    c_handler = logging.StreamHandler()  # Console handler
    f_handler = RotatingFileHandler('bruteforce.log', maxBytes=10000, backupCount=3)  # File handler
    c_handler.setLevel(logging.WARNING)  # Console logs warnings and above
    f_handler.setLevel(logging.INFO)     # File logs info and above

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

# Define a function that could raise an exception
def risky_function():
    try:
        # This will raise a ZeroDivisionError
        result = 1 / 0
    except ZeroDivisionError as e:
        # Log the exception with traceback information
        log.exception("An exception occurred: Division by zero")

# Main program
if __name__ == "__main__":
    # Setup the logger
    log = setup_logging()

    # Log different types of log messages
    log.debug('This is a debug message, typically useful for developers')
    log.info('This is an info message, generally informational statements')
    log.warning('This is a warning message, indicating something unexpected')
    log.error('This is an error message, indicating a problem')
    log.critical('This is a critical message, indicating a serious error')

    # Call the risky function to generate an exception
    risky_function()
