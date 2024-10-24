#!/usr/bin/env python3

def shrink(input_string):
    # Display the first eight characters of the string
    print(input_string[:8])

def enlarge(input_string):
    # Append 'Z' characters to make it a total of eight characters and display
    padding = 'Z' * (8 - len(input_string))
    print(input_string + padding)

import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there are parameters
if len(arguments) < 1:
    # Display "none" if there are less than 1 parameter
    print("none")
else:
    # Process each argument based on its length
    for arg in arguments:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)  # If exactly 8 characters, display directly