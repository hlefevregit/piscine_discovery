#!/usr/bin/env python3
import sys
import re

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check if there are exactly two parameters
if len(arguments) != 2:
    # Display "none" if there are not exactly two parameters
    print("none")
else:
    # Extract keyword and search string from arguments
    keyword = arguments[0]
    search_string = arguments[1]
    
    # Find all occurrences of the keyword in the search string
    occurrences = re.findall(keyword, search_string)
    
    # Count the number of occurrences
    count = len(occurrences)
    
    # Display the count of occurrences
    print(count)
