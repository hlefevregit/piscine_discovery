#!/usr/bin/env python3

number_str = input("Give me a number: ")
    
try:
    # Attempt to convert the input to a float
    number = float(number_str)
    
    # Check if the number is an integer (even if it is given as a float with .00)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
    