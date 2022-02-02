
#change to absolute value
number = float(input("Enter Amount:"))
absoluteValue= abs(number)

#multiply absolute nuumber by 100
centValue = absoluteValue * 100
print ('The absolute cent value of {} dollars is {}'.format (number,int(centValue)))