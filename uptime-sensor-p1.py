import subprocess
import time
import datetime

# Set a default IP address
default_ip = '192.168.0.190'
# Accept user input for the target IP address, use default if the input is empty
ip_address = input(f"Enter the target IP address (default {default_ip}): ") or default_ip

def ping_ip(ip):
    try:
        # On Windows, use '-n' instead of '-c'
        output = subprocess.check_output(['ping', '-n', '1', ip], stderr=subprocess.STDOUT, universal_newlines=True)
        return True
    except subprocess.CalledProcessError:
        return False

# Open the specified file to save the logs
with open('uptime_log_p1.txt', 'a') as log_file:
    while True:
        success = ping_ip(ip_address)
        status = "Network Active" if success else "No Response"
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        log_entry = f"{timestamp} {status} to {ip_address}\n"
        print(log_entry, end='')
        log_file.write(log_entry)
        log_file.flush()
        time.sleep(2)
# Resources 
[ChatGPT]
