import random

alphabets = "abcdefghijklmnopqrstuvwxyz"
string = ""
for i in range(5):
    string = string + random.choice(alphabets)
print(string)
