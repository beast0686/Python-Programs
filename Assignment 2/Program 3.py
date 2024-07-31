sentence = "The quick Brow Fox"
uc = 0
lc = 0
for letter in sentence:
    if letter.isupper():
        uc += 1
    if letter.islower():
        lc += 1
print("Uppercase characters:", uc)
print("Lowercase characters:", lc)
