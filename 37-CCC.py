#!/usr/bin/env python3
# Script Name:                  Ops Challenge: Cookie Capture Capades
# Author:                       E. Campos
# Date of latest revision:      FEB 2024
# Resource:                     Classmates & https://chat.openai.com/share/baf7c736-8491-42a5-9a66-4440e38e54d8
# Purpose:                      The pupose of this script is to demonstrate web scraping techniques and cookie management.

import requests

# The URL you will make the request to
url = "http://dvwa.local/login.php"

# Make the initial request to capture the cookies
response = requests.get(url)
cookies = response.cookies

# Display the cookies received
print("Cookies received:", cookies)

# Make a subsequent request, sending the cookies back to the server
response_with_cookies = requests.get(url, cookies=cookies)

# Display the server's response
print("Server response:", response_with_cookies.text)
