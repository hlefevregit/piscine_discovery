#!/usr/bin/env python3
import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there are parameters
if len(arguments) == 0:
    # Display "none" if there are no parameters
    print("none")
else:
    # Display the number of parameters
    print(f"parameters: {len(arguments)}")
    
    # Iterate through each parameter
    for param in arguments:
        # Display the parameter and its length
        print(f"{param}: {len(param)}")