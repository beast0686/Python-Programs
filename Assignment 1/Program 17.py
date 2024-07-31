sentence = input("Enter a string: ")
lc = 0
uc = 0
for letter in sentence:
    if letter.isupper():
        uc = uc + 1
    if letter.islower():
        lc = lc + 1
print("Uppercase:", uc)
print("Lowercase:", lc)