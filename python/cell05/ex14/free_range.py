#!/usr/bin/env python3
import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there are exactly two parameters
if len(arguments) != 2:
    # Display "none" if there are not exactly two parameters
    print("none")
else:
    # Convert parameters to integers
    try:
        start = int(arguments[0])
        end = int(arguments[1])
        
        # Construct the array using range
        result = list(range(start, end + 1))
        
        # Display the array
        print(result)
    
    except ValueError:
        # Handle if parameters cannot be converted to integers
        print("none")