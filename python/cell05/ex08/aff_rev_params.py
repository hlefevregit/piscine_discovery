#!/usr/bin/env python3
import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there are fewer than two parameters
if len(arguments) < 2:
    # Display "none" if there are fewer than two parameters
    print("none")
else:
    # Display all parameters in reverse order
    reversed_arguments = arguments[::-1]
    print(" ".join(reversed_arguments))
