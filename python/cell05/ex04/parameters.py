#!/usr/bin/env python3
import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Calculate the number of parameters
num_parameters = len(arguments)

# Display the number of parameters
print(f"Number of parameters: {num_parameters}.")