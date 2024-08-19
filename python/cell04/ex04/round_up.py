#!/usr/bin/env python3
import math

# Prompt the user for a number
number_str = input("Give me a number: ")

try:
    # Convert the input to a float
    number = float(number_str)
    
    # Round the number up to the nearest integer
    rounded_number = math.ceil(number)
    
    # Print the rounded number
    print(rounded_number)
except ValueError:
    print("Invalid input. Please enter a valid number.")