#!/usr/bin/env python3

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print(f"Hello, {name}! Welcome!")
    else:
        print("Error: The argument should be a string.")

# Example usages
greetings()  # No argument provided
greetings("Alice")  # Argument provided (valid string)
greetings(123)  # Argument provided (not a string)