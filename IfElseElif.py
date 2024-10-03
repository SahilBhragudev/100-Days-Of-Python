# appleprice = float(input("Enter apple price : "))
# budget = float(input("Enter budget : "))

# if ((budget - appleprice) >= 100):
#   print("Alexa ! Add apples in the cart")
# else:
#   print("Alexa !Do not Add apples in the cart")

# num = int(input("Enter the number : "))
# if (num < 0):
#   print("Number is negative")
# elif (num == 0):
#   print("Number is zero")
# else:
#   print("Number is positive")

# if (num < 0):
#   print("Number is negative")
# elif (num > 0):
#   if (num <= 10):
#     print("Number is between 0 nd 10")
#   elif (num > 10 and num <= 20):
#     print("Number is between 11 and 20")
#   else:
#     print("Number is greater than 20")
# else:
#   print("Number is zero")

# time = float(input("enter the current time : "))
# if (time < 12.00):
#   print("Good Morning")
# elif (time > 12.00 and time <= 16.00):
#   print("Good Afternoon")
# elif (time > 16.00 and time <= 20.00):
#   print("Good Evening")
# else:
#   print("Good Night")

import time

curr_time = input("Current time is : " + time.strftime('%H : %M'))
present_Hour = int(time.strftime('%H'))
print("Present time is : ", present_Hour)
if (present_Hour > 4 and present_Hour <= 12):
  print("Good Morning")
elif (present_Hour > 12 and present_Hour <= 17):
  print("Good AfterNoon")
elif (present_Hour > 17 and present_Hour <= 20):
  print("Good Evening")
else:
  print("good Night")
