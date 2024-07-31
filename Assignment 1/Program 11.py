# Rolling a dice

import random

seq = range(1, 6)
while True:
    input("Press enter to roll the die: ")
    rand = random.choice(seq)
    print("You got:", rand)