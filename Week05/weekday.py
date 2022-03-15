from datetime import datetime
today = datetime.today().isoweekday()
if 1 <= today <= 5:
    print("Yes, unfortunately today is a weekday.")

else:
    print ("It is the weekend, yay!")
