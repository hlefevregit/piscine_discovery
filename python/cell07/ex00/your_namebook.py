#!/usr/bin/env python3

def array_of_names(names_dict):
    # Initialize an empty array to store full names
    full_names = []
    
    # Iterate through the dictionary and construct full names
    for first_name, last_name in names_dict.items():
        # Capitalize the first letter of each name and construct the full name
        full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
        # Append the full name to the array
        full_names.append(full_name)
    
    return full_names

# Example dictionary of names
names_dict = {
    'john': 'doe',
    'jane': 'smith',
    'alice': 'johnson',
    'bob': 'brown'
}

# Call the array_of_names method and get the result
full_names_array = array_of_names(names_dict)

# Print the result
print(full_names_array)