def calculate_sum(number):
    number = number + calculate_sum(number-1)


calculate_sum(10)