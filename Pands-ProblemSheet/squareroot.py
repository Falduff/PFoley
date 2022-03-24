def squareroot(number, number_integers = 100):
    x = float(number)
    for i in range(number_integers):
        number = 0.5 * (number + x / number)
    return number

x = int(input("Please enter a positive number:"))
print ("The square root of 14.5 is approx:" ,squareroot (x))