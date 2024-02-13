#!/usr/bin/python3

# Script Name:                  Event Logging Tool p.1
# Author:                       E Campos
# Date of latest revision:      FEB2024
# Purpose:                      The purpose of this script is to integrate logging into an existing Python tool to record events, facilitate debugging, and provide actionable information to support security operations and automated systems.
# Resources:                    [Python Logging Tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial) / [What Are stdin, stdout, and stderr on Linux?](https://www.howtogeek.com/435903/what-are-stdin-stdout-and-stderr-on-linux/) / [Logging Module in Python](https://dotnettutorials.net/lesson/logging-module-in-python/) / Classmates Juan Cano / Class Demo

import logging
# Configure logging settings to write to collections_tool.log
logging.basicConfig(filename='collections_tool.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# Log the start of the script
logging.debug('Starting script execution.')
# Create a list
my_list = ['junk', 'stuff', 'house', 'car', 'cat', 'window', 'tree', 'pipe', 'dragonfruit', 'grape', 'nuts']
# Log the creation of the list
logging.debug('List created: %s', my_list)
# Print the entire list/array
print(my_list)
# Print the element at index 3 (fourth element) of the list/array called my_list
print(my_list[3])
# Print the last item in the list
print(my_list[-1])
# Print the fourth element on the list (again, as done above)
print(my_list[3])
# Print the sixth through the tenth element of the list (elements from index 5 to the end)
print(my_list[5:])
# Change the value of the seventh element (index 6) to "onion"
my_list[6] = "onion"
# Log the modification of the list
logging.debug('Modified list element at index 6 to "onion".')
# Print the entire list to show the updated list
print(my_list)
# Log the final state of the list
logging.debug('Final list: %s', my_list)
# Log the end of script execution
logging.debug('Script execution completed.')