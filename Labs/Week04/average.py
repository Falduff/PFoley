numbers = []

number = int(input("Enter Number (0 quits):"))

while number != 0:
    numbers.append(number)

    number = int(input("Enter Number (0 quits):"))

average = float(sum(numbers))/ len(numbers)
print ("The average is {}".format(average))