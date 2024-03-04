#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Cookie Capture Capades
# Author:                       E. Campos
# Date of latest revision:      FEB 2024
# Resource:                     Classmates & https://chat.openai.com/share/baf7c736-8491-42a5-9a66-4440e38e54d8
# Purpose:                      The pupose of this script is to demonstrate web scraping techniques and cookie management.

import requests

# The URL from where we need to capture cookies
url = "http://example.com"  # Replace with the actual URL

# Create a session object to persist cookies across requests
session = requests.Session()

# Make an initial GET request to capture cookies
initial_response = session.get(url)

# Display the captured cookies
print("Captured cookies from the initial response:")
for cookie in session.cookies:
    print(f"Cookie: {cookie.name}, Value: {cookie.value}")

# Now, send the captured cookies back to the server in a new request
# The session object automatically handles this
response_with_cookies = session.get(url)

# Display the server's response
print("Server response after sending cookies:")
print(response_with_cookies.text)
