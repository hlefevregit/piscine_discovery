#!/usr/bin/env python3

# Ask the user for the first number
num1 = float(input("Please enter the first number: ").strip())

# Ask the user for the second number
num2 = float(input("Please enter the second number: ").strip())

# Perform calculations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "undefined"  # Handle division by zero

# Display the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")
