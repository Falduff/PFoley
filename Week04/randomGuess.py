#random number genrator
import random
a = random.randint(1,100)

#guess2.py
numberToGuess = a

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < a:
        print ("Too low!")
    if guess > a:
        print ("Too high!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was", numberToGuess)