
def multiply_binary_with_bin(num1, num2):
    # Convert binary numbers to integers
    int_num1 = int(num1, 2)
    int_num2 = int(num2, 2)

    # Multiply the integers
    result = int_num1 * int_num2

    # Convert the result back to binary
    binary_result = bin(result)

    return binary_result


def multiply_binary_without_bin(num1, num2):
    # Convert binary numbers to integers manually
    int_num1 = int(num1, 2)
    int_num2 = int(num2, 2)

    # Multiply the integers
    product = 0
    while int_num2 > 0:
        if int_num2 & 1:
            product += int_num1
        int_num1 <<= 1
        int_num2 >>= 1

    # Convert the result back to binary manually
    binary_result = ''
    while product > 0:
        binary_result = str(product % 2) + binary_result
        product //= 2

    return binary_result


# Test the functions
binary_num1 = input("Enter first binary no.: ")
binary_num2 = input("Enter second binary no.: ")

# Method 1: Using bin() function
result_with_bin = multiply_binary_with_bin(binary_num1, binary_num2)
print(f"The product of {binary_num1} and {binary_num2} using bin() function is: {result_with_bin}")

# Method 2: Without using pre-defined functions
result_without_bin = multiply_binary_without_bin(binary_num1, binary_num2)
print(f"The product of {binary_num1} and {binary_num2} without using bin() function is: {result_without_bin}")
