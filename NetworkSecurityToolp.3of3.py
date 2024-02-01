#!/usr/bin/env python3

# Script Name:                  Network Security Tool with Scapy p. 3 of 3
# Author:                       E Campos
# Date of latest revision:      22/01/2024
# Purpose:                      Ping a specified IP address to check for host availability and then perform a TCP port scan to identify open ports if the host is responsive.
# Resources:                    ChatGPT
from scapy.all import sr1, ICMP, IP, TCP, conf, L3RawSocket

# Suppress Scapy IPv6 warning and use IPv4 only
conf.L3socket = L3RawSocket
conf.ipv6_enabled = False

# Function to perform an ICMP ping to check if the host is up
def icmp_ping(host_ip):
    icmp_packet = IP(dst=host_ip) / ICMP()
    resp = sr1(icmp_packet, timeout=1, verbose=0)
    return resp is not None

# Function to perform a TCP port scan on the given IP address
def tcp_port_scan(host_ip, port_range):
    open_ports = []
    for port in port_range:
        tcp_syn_packet = IP(dst=host_ip) / TCP(dport=port, flags='S')
        resp = sr1(tcp_syn_packet, timeout=1, verbose=0)
        if resp and resp.haslayer(TCP) and resp.getlayer(TCP).flags & 0x12:  # SYN-ACK flags
            open_ports.append(port)
    return open_ports

# Main execution function
def main():
    target_ip = input("Please enter the IP address to target: ")
    print(f"Pinging {target_ip} to check if host is up...")
    
    if icmp_ping(target_ip):
        print(f"Host {target_ip} is up. Starting TCP port scan...")
        port_range = range(1, 1025)  # Scanning the well-known ports
        open_ports = tcp_port_scan(target_ip, port_range)
        if open_ports:
            print(f"Open ports on {target_ip}: {', '.join(str(port) for port in open_ports)}")
        else:
            print("No open ports found on the target host.")
    else:
        print(f"Host {target_ip} is down or not responding to pings.")

if __name__ == "__main__":
    main()
