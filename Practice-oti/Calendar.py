
# How to determine whether a year is a leap year
# To determine whether a year is a leap year, follow these steps:

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

# Year = int(input("Enter Year : "))
# det4 = Year % 4
# det100 = Year% 100
# det400 = Year % 400
# if det4 == 0:
#     if det100== 0 :
#         if det400 == 0:
#          print("The year is a leap year (It has 365 days)")
# else:
#     print("The year is not a leap year (It has 365 days)")

# Year = int(input("Enter Year : "))
# det4 = Year % 4
# det100 = Year% 100
# det400 = Year % 400
# if det4 == det100 == det400 == 0:
#   print("The year is a leap year (It has 365 days)")
# else:
#     print("The year is not a leap year (It has 365 days)")

Year = int(input("Enter Year : "))
det4 = Year % 4
det100 = Year% 100
det400 = Year % 400
if det4 == 0:
    print("The year is a leap year (It has 365 days)")
elif det100 == 0:
        print("The year is a leap year (It has 365 days)")
elif det400 == 0 :
    print("The year is a leap year (It has 365 days)")
else:
    print("The year is not a leap year (It has 365 days)")


