sample_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
unique_list = []
for element in sample_list:
    if element not in unique_list:
        unique_list.append(element)
print(unique_list)