#!/usr/bin/python3

# Script Name:                  Event Logging Tool p.1
# Author:                       E Campos
# Date of latest revision:      FEB2024
# Purpose:                      This script configures logging with a custom logger named "my_logger", sets up basic logging settings to write log messages to a file named "bruteforce.log", and logs informational, warning, and debug messages to the configured log file.
# Resources:                    Classmates Christen R., ChatGPT
#                               https://chat.openai.com/share/9a32f1fb-287a-438d-9ff2-34b5341a2fe0


import logging
from logging.handlers import TimedRotatingFileHandler
import os
import time

# Configure logging
def configure_logging():
    logger = logging.getLogger('myTimedLogger')
    logger.setLevel(logging.DEBUG)
    handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

# Log and print messages
def log_and_print(logger, message, level):
    if level == 'warning':
        logger.warning(message)
    elif level == 'info':
        logger.info(message)
    # Add more levels as needed
    print(message)

# Execute a command and log output
def execute_command(logger, command):
    logger.info(f"Executing command: {command}")
    os.system(command)

# List operations
def list_operations(logger):
    # Define your list here and perform operations
    my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]
    # Perform your operations and log as needed using log_and_print

def main():
    logger = configure_logging()
    
    # Example usage:
    log_and_print(logger, "Aye Aye Ma'am", 'warning')
    execute_command(logger, "ls -al")
    list_operations(logger)
    # Add more function calls as needed

if __name__ == "__main__":
    main()
