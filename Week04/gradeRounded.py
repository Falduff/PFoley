percentage = float(input("Enter the percentage:"))
roundedpercentage = (round(percentage))

if roundedpercentage < 0 or roundedpercentage > 100:
    print ("Enter Percentage")
elif roundedpercentage < 40.0: 
    print ("Fail")
elif roundedpercentage < 50:
    print ("Pass")
elif roundedpercentage < 60:
    print ("Merit 1")
elif roundedpercentage < 70:
    print ("Merit 2")
else:
    print ("Distinction")