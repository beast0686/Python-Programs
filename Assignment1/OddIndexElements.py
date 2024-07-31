def display_odd_index_elements(input_list):
    print("Elements at odd index positions:")
    for i in range(1, len(input_list), 2):
        print(input_list[i])


# Given list
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Display elements at odd index positions
display_odd_index_elements(given_list)
