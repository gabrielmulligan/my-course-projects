# problem set #2 16th Mar 2019
# check does today begin with the letter T
# get the current date and time
import datetime
# check does today start with T
# weekday 0 = Monday and weekday 7 = Sunday so 1 or 3 must be Tues or Thurs
# we use an if and or to check for 1 and 3
if datetime.datetime.today().weekday() == 1 or datetime.datetime.today().weekday() == 3:
  # condition if today is true i.e. we are in Day 1 (Tue) or Day 3 (Thur)
  print("Yes, today begins with the letter T")
# condition if False, i.e. any other day other than Tue or Thur
else:
  print ("No, today, doesn't begin with T")