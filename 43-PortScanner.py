#!/usr/bin/python3

# Script Name:                  Event Logging Tool p.1
# Author:                       E Campos
# Date of latest revision:      Mar2024

# Purpose:                      The purpose of this Python script is to utilize the socket module for building a tool that can scan and identify open ports on a network, a fundamental skill in cybersecurity for assessing vulnerabilities.
import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
TIMEOUT = 10
sockmod.settimeout(TIMEOUT)

hostip = input("Enter host IPv4: ")
portno = int(input("Enter port: "))

def portScanner():
    if sockmod.connect_ex((hostip, portno)) != 0:
        print("Port closed")
    else:
        print("Port open")

portScanner()