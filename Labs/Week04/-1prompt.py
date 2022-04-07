# How would you use a while loop to modify isEven so that it keeps prompting 
# the user for a number until the user enters -1

#isEven:
number = int(input("enter an integer:"))
numbers = []
while number != -1:
    numbers.append(number)

    number = int(input("enter an integer (-1 to quit):"))

if (number % 2) == 0:
    print ("{} is an even number".format(number))
    
else:
    print("{} is an odd number".format(number))