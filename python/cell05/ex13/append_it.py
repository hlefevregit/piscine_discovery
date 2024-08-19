#!/usr/bin/env python3
import sys
import re

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there are parameters
if len(arguments) == 0:
    # Display "none" if there are no parameters
    print("none")
else:
    # Iterate through each parameter
    for param in arguments:
        # Check if the parameter already ends with "ism"
        if re.search(r"ism$", param):
            continue  # Skip this parameter
        
        # Append "ism" to the parameter and display it
        print(param + "ism")