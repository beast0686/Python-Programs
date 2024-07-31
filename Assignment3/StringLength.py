def find_string_length(input_string):
    count = 0
    for char in input_string:
        count += 1
    return count


# Test the function with the string "refrigerator"
input_string = input("Enter String: ")
length = find_string_length(input_string)
print("Length of the string without using len() function:", length)
