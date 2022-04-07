percentage = float(input("Enter the percentage"))

if percentage < 0 or percentage > 100:
    print ("Enter Percentage")
elif percentage < 40.0: 
    print ("Fail")
elif percentage < 50:
    print ("Pass")
elif percentage < 60:
    print ("Merit 1")
elif percentage < 70:
    print ("Merit 2")
else:
    print ("Distinction")