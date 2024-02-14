#!/usr/bin/python3

# Script Name:                  Event Logging Tool p.1
# Author:                       E Campos
# Date of latest revision:      FEB2024
# Purpose:                      This script configures logging with a custom logger named "my_logger", sets up basic logging settings to write log messages to a file named "bruteforce.log", and logs informational, warning, and debug messages to the configured log file.
# Resources:                    Classmates Christen R., ChatGPT
#                               https://chat.openai.com/share/9a32f1fb-287a-438d-9ff2-34b5341a2fe0
# Purpose: In Python, Logging capabilities to your Python tool with log rotation based on size.

import logging
from logging.handlers import RotatingFileHandler

# Configure logging with rotation
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
logFile = 'my_tool.log'

# Create a handler that writes log messages to a file, with a maximum
# log size of 1MB, and a backup count of 3.
handler = RotatingFileHandler(logFile, mode='a', maxBytes=1*1024*1024, 
                              backupCount=3, encoding=None, delay=0)
handler.setFormatter(log_formatter)
handler.setLevel(logging.DEBUG)

logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

def main():
    logger.info('Starting my_tool')
    try:
        # Your tool's main functionality here
        result = 10 / 0  # Intentionally induce a ZeroDivisionError
    except ZeroDivisionError as e:
        logger.error('Encountered a division by zero error: %s', e)
    except Exception as e:
        logger.exception('An unexpected error occurred: %s', e)
    finally:
        logger.info('Exiting my_tool')

if __name__ == "__main__":
    main()