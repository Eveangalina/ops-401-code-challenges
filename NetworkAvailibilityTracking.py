#!/usr/bin/env python3

# Script Name:                  Uptime Sensor Tool
# Author Name:                  Eveangalina Campos
# Date of latest revision:      01/21/2024
# Purpose:                      Network availability tracking with Uptime Sensor Tool

import subprocess
import time
import datetime
import logging
import sys

# Initialize logging
logging.basicConfig(filename='uptime_sensor.log', level=logging.INFO, format='%(asctime)s %(levelname)s:%(message)s')

# Configurable Parameters
default_ip = '192.168.0.190'
ping_interval = 2  # in seconds
log_filename = 'uptime_log_p1.txt'

def parse_args():
    """ Parse command-line arguments for flexibility. """
    if len(sys.argv) > 1:
        return sys.argv[1], int(sys.argv[2]), sys.argv[3]
    return default_ip, ping_interval, log_filename

def ping_ip(ip):
    """ Ping the given IP address and return True if successful. """
    try:
        output = subprocess.check_output(['ping', '-n', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError as e:
        logging.error(f"Ping failed: {e}")
        return False
    except Exception as e:
        logging.error(f"Unexpected error during ping: {e}")
        return False

if __name__ == "__main__":
    ip_address, interval, logfile = parse_args()

    with open(logfile, 'a') as log_file:
        while True:
            success = ping_ip(ip_address)
            status = "Network Active" if success else "No Response"
            log_entry = f"{datetime.datetime.now()} {status} to {ip_address}\n"
            print(log_entry, end='')
            log_file.write(log_entry)

            time.sleep(interval)
