#!/usr/bin/env python3

def upcase_it(input_string):
    return input_string.upper()


input_str = input("Enter a string: ")
result = upcase_it(input_str)
print("Uppercase:", result)