# n = -9
# while n < 0:
#     n += 1
#     print (n)

# print (n)

# import time
# from winsound import Beep

# minute = int(input("How many minutes countdown do you need? "))
# while minute > 0:
#     second = 60
#     minute -= 1
#     while second > 0:
#             Beep (1000, 200)
#             second -= 1
#             print (f"{minute}:{second} minute(s) left\r", end = "")
#             time.sleep(1)

# print ("Time up!                          ")
# Beep(1000, 2000)
# #Do for minutes and seconds.



import random

while True:
    input ("Press Enter to continue")

    number = random.randint(1, 6)
    number2 = random.randint(1, 6)
    print (number, number2)
    if number == number2 == 6:
        print ("Congratulations!")
        break
    else:
        print ("Sorry try again.")
    
