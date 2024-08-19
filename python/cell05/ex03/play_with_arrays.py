#!/usr/bin/env python3

# Define the original array of numbers
original_array = [2, 8, 9, 48, 8, 22, -12, 2]

# Create a new array by adding 2 to each value of the original array that is greater than 5
new_array = [x + 2 for x in original_array if x > 5]

# Remove duplicates by converting the list to a set and back to a list
unique_new_array = list(set(new_array))

# Display both arrays on the screen
print("Original array:", original_array)
print("New array (only values > 5, no duplicates):", unique_new_array)