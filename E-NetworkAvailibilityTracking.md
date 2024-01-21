### Network Availability Email Notification Tool

*This Python script is designed to monitor the network availability of a specified IP address continuously. When run, it performs the following actions:*

- **Pings a Target IP Address:** At regular intervals, the script uses the ping command native to Windows to check the network connectivity to the specified IP address.

- **Logs Activity:** It records the results of each ping attempt, including a timestamp and the network status ("Active" or "Inactive"), to a log file named uptime_log.txt.

- **Email Notifications**: If a change in network status is detected <br/> (e.g., the target goes from reachable to unreachable or vice versa),<br/> the script sends an email notification to a pre-specified administrator's email address. This notification includes the time of the status change and the new status.

- **User Inputs:** Upon initiation, the script prompts the user to enter the administrator’s email address for notifications and the target IP address to monitor.

- **Graceful Termination:** The script can be stopped manually by the user with a KeyboardInterrupt (usually by pressing Ctrl+C in the command line interface), at which point it will output a "Monitoring stopped." message. <br/>
This tool is particularly useful for system administrators who need to ensure that critical network resources remain online, or who need to be alerted immediately upon any changes in network availability.
