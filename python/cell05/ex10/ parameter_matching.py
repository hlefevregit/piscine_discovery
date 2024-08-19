#!/usr/bin/env python3
import sys

# Get the list of command line arguments, excluding the script name
arguments = sys.argv[1:]

# Check the number of parameters
if len(arguments) != 1:
    # Display "none" if the number of parameters is not 1
    print("none")
else:
    # Prompt the user to enter a word
    user_word = input("Enter a word: ")
    
    # Get the parameter passed
    parameter = arguments[0]
    
    # Compare user input with the parameter
    if user_word == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
