#!/usr/bin/python3

# Script Name:                  Event Logging Tool p.1
# Author:                       E Campos
# Date of latest revision:      FEB2024
# Purpose:                      StreamHandler and FileHandler 
#                               Incorporating logging capabilities using handlers for both timed rotating file logs and regular file logs, alon with logging to the terminal.
#                               Demonstrate the manipulation of lists and the use of various list methods, including basic operations and involving tuples, sets, and dictionaries.                    

# Resource:                     https://chat.openai.com/share/6b684dac-908a-45bd-8ca2-d00024e04158
# Team member:                  Rodolfo Gonzalez, Juan Cano

import logging
from logging.handlers import TimedRotatingFileHandler
import time

# Function to configure logging
def configure_logging():
    logger = logging.getLogger('myAppLogger')
    logger.setLevel(logging.DEBUG)

    # Timed rotating file handler
    timed_handler = TimedRotatingFileHandler('timed_app.log', when="midnight", interval=1, backupCount=7)
    timed_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # File handler
    file_handler = logging.FileHandler('app.log')
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Add handlers to logger
    logger.addHandler(timed_handler)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Function to perform logging
def perform_logging(logger):
    for i in range(5):
        logger.warning(f"Aye Aye Ma'am {i}")
        time.sleep(1)

# Main function
def main():
    logger = configure_logging()
    perform_logging(logger)

if __name__ == "__main__":
    main()
