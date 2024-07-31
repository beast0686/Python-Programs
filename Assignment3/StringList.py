def rearrange_list_by_occurrences(input_list, user_string):
    # Count occurrences of user string in each element of the list
    occurrences = [(element, element.count(user_string)) for element in input_list]

    # Sort the list based on the count of occurrences in descending order
    sorted_list = sorted(occurrences, key=lambda x: x[1], reverse=True)

    # Extract elements from sorted list
    rearranged_list = [element[0] for element in sorted_list]

    return rearranged_list


# Example list containing only strings
example_list = ["no bun", "bug bun bug bun bug bug", "bunny bug", "buggy bug bug buggy"]

# Input string from the user
user_string = input("Enter a string: ")

# Rearrange the list based on occurrences of the user string
output_list = rearrange_list_by_occurrences(example_list, user_string)

# Print the rearranged list
print("OUTPUT LIST:", output_list)
