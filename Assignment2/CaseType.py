def count_upper_lower(string):
    upper_count = 0
    lower_count = 0
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    print("No. of Upper case characters:", upper_count)
    print("No. of Lower case Characters:", lower_count)


# Test the function with the sample string
sample_string = input("Enter String: ")
count_upper_lower(sample_string)
