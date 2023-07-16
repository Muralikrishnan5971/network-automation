import random
import calendar
for n in range(1, 11):
    month = calendar.month_name[n]
    print(month +", "+str(random.randint(300, 400))+", "+ 
          str(random.randint(300, 400))+", "+ 
          str(random.randint(300, 400)))
    