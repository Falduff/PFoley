numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
    if guess < 30:
        print ("Too low!")
    if guess > 30:
        print ("Too high!")
    guess = int(input("Please guess again:"))

print ("Well done! Yes the number was", numberToGuess)