#!/usr/bin/env python3
import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there is exactly one parameter
if len(arguments) != 1:
    # Display "none" if there are not exactly one parameter
    print("none")
else:
    # Get the parameter passed (the string)
    input_string = arguments[0]
    
    # Count occurrences of "z" in the string
    count_z = input_string.count("z")
    
    # If there are no "z" characters, display "none"
    if count_z == 0:
        print("none")
    else:
        # Display "z" for each occurrence of "z" in the string
        print("z" * count_z)