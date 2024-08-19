#!/usr/bin/env python3
import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there is exactly one parameter
if len(arguments) == 1:
    # Display the parameter in uppercase
    print(arguments[0].upper())
else:
    # Display "none" if the number of parameters is not 1
    print("none")