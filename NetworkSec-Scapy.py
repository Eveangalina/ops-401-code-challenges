#!/usr/bin/env python3
# Script Name:                  Ops 12: Network Security Tool with Scapy Part 2 of 3
# Author:                       Eveangalina Campos
# Date of latest revision:      01/25/2024
# Purpose:                      Performs network scanning, including TCP port range scanning and ICMP ping sweeps, to ID open ports and active hosts on a network
# Resources:                    https://chat.openai.com

from scapy.all import sr1, ICMP, IP, TCP, send
import ipaddress

# User Menu
# This section implements the user menu which allows the user to choose between
# TCP Port Range Scanner mode and ICMP Ping Sweep mode.
def main():
    while True:
        print("\nSelect a mode:")
        print("1. TCP Port Range Scanner")
        print("2. ICMP Ping Sweep")
        print("3. Exit")
        mode = input("Enter the mode (1/2/3): ")

        # TCP Port Range Scanner Mode
        # This part of the code performs the TCP Port Range Scanner operation.
        if mode == '1':
            host_ip = input("Enter the host IP to scan: ")
            ports = input("Enter the port range (e.g., 20-80) or specific ports separated by commas: ")
            # Parsing the port range or specific ports
            if '-' in ports:
                start_port, end_port = map(int, ports.split('-'))
                port_list = range(start_port, end_port + 1)
            else:
                port_list = [int(port.strip()) for port in ports.split(',')]
            tcp_port_scan(host_ip, port_list)

        # ICMP Ping Sweep Mode
        # This part of the code performs the ICMP Ping Sweep operation.
        elif mode == '2':
            network = input("Enter the network address with CIDR (e.g., 192.168.1.0/24): ")
            icmp_ping_sweep(network)

        elif mode == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid mode. Please choose a number between 1 and 3.")

# The TCP Port Range Scanner Function
def tcp_port_scan(host_ip, port_list):
    for port in port_list:
        packet = IP(dst=host_ip)/TCP(dport=port, flags='S')
        response = sr1(packet, timeout=2, verbose=False)
        # ...

# The ICMP Ping Sweep Function
# This function prompts the user for a network address including CIDR block
# and performs a ping sweep on all addresses in the network, handling the response
# as per the requirements.
def icmp_ping_sweep(network):
    online_hosts = 0
    network = ipaddress.ip_network(network, strict=False)
    for ip in network.hosts():
        resp = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=False)
        if resp is None:
            print(f"{ip} is down or unresponsive")
        elif (resp.haslayer(ICMP) and resp.getlayer(ICMP).type == 3 and resp.getlayer(ICMP).code in [1, 2, 3, 9, 10, 13]):
            print(f"{ip} is actively blocking ICMP traffic.")
        else:
            print(f"{ip} is responding.")
            online_hosts += 1
    print(f"Total hosts online: {online_hosts}")

# Main function execution
if __name__ == "__main__":
    main()
