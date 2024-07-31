# Print even numbers from the list

items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_items = []
for item in items:
    if item%2 == 0:
        even_items.append(item)
print(even_items)