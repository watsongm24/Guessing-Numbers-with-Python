#Number Guessing Game using Python

import random

n = random.randrange(1, 12)
guess = int(input("Input the gessing number: "))
while n != guess:
    if guess < n:
        print("Too Low")
        guess = int(input("Enter the number again: "))
    elif guess > n:
        print("Too high")
        guess = int(input("Enter the number again: "))
    else:
        break
print("You got it right")