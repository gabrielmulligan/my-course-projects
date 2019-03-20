# Ian McLoughlin, 2018-02-01
# Is it Saturday?

import datetime

if datetime.datetime.today().weekday() == 5:
  print("Yay! It is Saturday.")
else:
  print("Unfortunately it is not Saturday.")