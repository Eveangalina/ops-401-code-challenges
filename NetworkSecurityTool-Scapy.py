#!/usr/bin/env python3

# Script Name:                  Network Security Tool with Scapy
# Author:                       Evengalina Campos
# Date of latest revision:      22/01/2024      
# Purpose:                      Assess the status of TCP ports on a specified host (IP address)

from scapy.all import *

def tcp_port_scan(target_ip, port_range):
    for port in port_range:
        # Create a TCP packet with SYN flag
        tcp_packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        
        # Send the packet and wait for a reply
        response = sr1(tcp_packet, timeout=1, verbose=0)
        
        if response:
            # Check if the port is open (SYN-ACK received)
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                # Send a RST packet to close the connection
                rst_packet = IP(dst=target_ip) / TCP(dport=port, flags="R")
                send(rst_packet, verbose=0)
                print(f"Port {port} is open.")

            # Check if the port is closed (RST received)
            elif response.haslayer(TCP) and response.getlayer(TCP).flags == 0x14:
                print(f"Port {port} is closed.")
        else:
            # No response indicates the port is filtered and silently dropped
            print(f"Port {port} is filtered and silently dropped.")

# Example usage
target_ip = "192.168.1.1"  # Replace with the actual target IP
port_range = [22, 80, 443]  # Example port range, replace with your desired ports

tcp_port_scan(target_ip, port_range)
