#!/bin/bash

# Check if argument was passed
if [ $# -eq 0 ]; then
    echo "Error: You need to provide an argument indicating the number of times the message will be displayed"
    exit 1
fi

# Assign the first argument to a variable
times=$1

# Verify that the parameter is a positive integer
if ! [[ "$times" =~ ^[0-9]+$ ]]; then
    echo "Error: The parameter must be a positive integer"
    exit 1
fi

# Loop to show the message
for (( i=0; i<times; i++ )); do
    echo "This looks good, @alrodri2!"
done

