# Demonstrating string operations

# Example string
my_string = "hello world"

# str.endswith() - checks if the string ends with a specified suffix
print("Ends with 'world':", my_string.endswith("world"))
print("Ends with 'hello':", my_string.endswith("hello"))

# str.capitalize() - returns a copy of the string with its first character capitalized
print("Capitalized string:", my_string.capitalize())

# str.replace() - returns a copy of the string with all occurrences of a substring replaced with another substring
print("Replacing 'world' with 'universe':", my_string.replace("world", "universe"))

# str.find() - returns the lowest index of the substring if found, -1 otherwise
print("Index of 'world':", my_string.find("world"))
print("Index of 'universe':", my_string.find("universe"))

# String concatenation
new_string = my_string + " of Python"
print("Concatenated string:", new_string)

# Indexing
print("First character:", my_string[0])
print("Last character:", my_string[-1])

# Range and slicing
print("Slicing from index 1 to 5:", my_string[1:5])
print("Slicing from index 6 onwards:", my_string[6:])
print("Slicing from index 3 to 8 with step 2:", my_string[3:8:2])
