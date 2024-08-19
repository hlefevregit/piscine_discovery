#!/usr/bin/env python3
import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there are any parameters
if arguments:
    # Display the first parameter
    print(arguments[0])
else:
    # Display "none" if there are no parameters
    print("none")
