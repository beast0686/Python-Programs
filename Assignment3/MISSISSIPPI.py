word = "MISSISSIPPI"

# Initialize an empty dictionary to store counts
letter_counts = {}

# Count occurrences of each letter in the word
for letter in word:
    if letter in letter_counts:
        letter_counts[letter] += 1
    else:
        letter_counts[letter] = 1

# Print the dictionary containing counts of each letter
print("Counts of each letter in the word 'MISSISSIPPI':")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
