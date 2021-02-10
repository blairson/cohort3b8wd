# # python program to check leap year 

# How to determine whether a year is a leap year 
# step to follow 
# 1. if the year is evenly divisible by 4, go to step2. otherwise, go to step 5.
# 2. if the yearis evenly divisible by 100,go to step 3. otherwise go to step 4
# 3. if the year is evenly divisible by 400, go to step 4. otherwise go to step 5.
# 4. The year is a leap year (it has 366 days)
# 5. the year is not a leap year(if has 365 days)

# year = int (input ("please Enter year: " ))
# if (year % 4 ) == 0:
#     if (year % 100 ) == 0:
#         if (year % 400 ) == 0:
#             print ("{0} is a leap year".format (year))
#         else: 
#             print ("{0} is not a leap year".format (year)) 
#     else: 
#             print ("{0} is a leap year".format (year)) 
# else: 
#             print ("{0} is a not leap year".format (year)) 
import time

x = int (input ("enter time: "))
while x:
    x -= 1
    time.sleep (1)
    print (x)
    