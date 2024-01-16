# Import necessary libraries
import os
import time
import smtplib
from email.message import EmailMessage

def ping_host(target_ip):
    # Windows ping command
    return os.system(f"ping -n 1 {target_ip} > NUL")

def send_email(sender_email, password, recipient_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

if __name__ == "__main__":
    sender_email = "CamposCyberSec@gmail.com"
    password = 'hdgo chbe pbnu mbnr' # App password for the email
    recipient_email = input("Enter the administrator's email address for notifications: ")
    
    target_ip = input("Enter the target IP address to monitor: ")
    log_filename = "uptime_log.txt"
    
    previous_status = None

    try:
        with open(log_filename, "a") as log_file:
            while True:
                exit_code = ping_host(target_ip)
                current_status = "Active" if exit_code == 0 else "Inactive"
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]

                if current_status != previous_status and previous_status is not None:
                    subject = f"Status Change Detected for {target_ip}"
                    body = f"{timestamp}: Host {target_ip} changed status from {previous_status} to {current_status}"
                    send_email(sender_email, password, recipient_email, subject, body)

                print(f"{timestamp} Network {current_status} to {target_ip}")
                log_file.write(f"{timestamp} Network {current_status} to {target_ip}\n")
                log_file.flush()

                previous_status = current_status
                time.sleep(10) # Adjust the sleep time as needed

    except KeyboardInterrupt:
        print("Monitoring stopped.")
# Resources ChatGPT