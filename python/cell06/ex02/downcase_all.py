#!/usr/bin/env python3

def downcase_it(input_string):
    return input_string.lower()

import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there are parameters
if len(arguments) == 0:
    # Display "none" if there are no parameters
    print("none")
else:
    # Apply downcase_it method to each parameter and display
    for param in arguments:
        result = downcase_it(param)
        print(f"Lowercase of '{param}': {result}")