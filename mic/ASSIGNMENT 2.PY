# # # python program to check leap year 

# # How to determine whether a year is a leap year 
# # step to follow 
# # 1. if the year is evenly divisible by 4, go to step2. otherwise, go to step 5.
# # 2. if the yearis evenly divisible by 100,go to step 3. otherwise go to step 4
# # 3. if the year is evenly divisible by 400, go to step 4. otherwise go to step 5.
# # 4. The year is a leap year (it has 366 days)
# # 5. the year is not a leap year(if has 365 days)

# # year = int (input ("please Enter year: " ))
# # if (year % 4 ) == 0:
# #     if (year % 100 ) == 0:
# #         if (year % 400 ) == 0:
# #             print ("{0} is a leap year".format (year))
# #         else: 
# #             print ("{0} is not a leap year".format (year)) 
# #     else: 
# #             print ("{0} is a leap year".format (year)) 
# # else: 
# # #             print ("{0} is a not leap year".format (year)) 
# # import time  
# from winsound import Beep
# # seconds_count = int (input ("enter time: "))
# # while seconds_count > 0:
# #     seconds_count -= 1
# #     time.sleep (2)
# #     print (seconds_count)
# #     Beep(500, 200)

# # # minutes and seconds countdown print on same line
# # # minutes = int (input("enter time in minute: "))
# # # while minutes > 0:
# # #     seconds = 60 
# # #     minutes -= 1
# #     while seconds > 0:
# #         seconds -= 1
# #         print (f"{minutes} : {seconds}")
# #         time.sleep(1)


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# # minutes and seconds countdown print on same line
# # minutes = int (input("enter time in minute: "))
# # while minutes > 0:
# #     seconds = 60 
# #     minutes -= 1
# #     while seconds > 0:
# #         seconds -= 1
# #         print (f"{minutes} : {seconds} ", sep = "" , end = "")
# #         time.sleep(1)
    
# #         print ("\r", end = "")
# #         Beep (1000, 500)
# # print ("hello")

# # hours = int (input("enter time in hours: "))
# # while hours > 0:
# #     hours -= 1
# #     minutes = 60 
    
# #     while minutes > 0:
# #         minutes -=1
# #         seconds  = 60
# #         while seconds > 0:
# #             seconds -= 1
# #         print (f" {hours} : {minutes} : {seconds} ", sep = "" , end = "")
# #         time.sleep(1)
# #         print ("\r", end = "")
# #         Beep (1000, 500)

# import random

# # while True:

# #      input("PRESS ENTER TO ROLL: ")

# #      die1 = random.randint(1,6)
# #      die2 = random.randint(1,6)

# #      print (f"DIE1-  {die1} : {die2}")

# #      if die1 == die2 == 6:
# #          print ("congratulations you got siki 2".upper())
# #          break
# #      else:
# #         print ("sorry try again...!!!".upper())

# # while True:

# #      input("PRESS ENTER TO ROLL: ")

# #      die1 = random.randint(1,6)
# #      die2 = random.randint(1,6)

# #      print ("DIE1-", die1)
# #      print ("DIE2-", die2)
# #      Beep(1000, 300)
# #      if die1 == die2 == 6:
# #          print ("congratulations you got siki 2".upper())
# #          break
# #      else:
# #         print ("oh oh sorry try again...!!!".upper())
 
# # a  = []
# # for i in ["A","B","C","A","B","C","A","B","C"]:
# #     if i == "C":
# #         a.append(i)
# #         print("".join (a))
# # for i in range (3):
# #     x = input ("enter ABC :" )
# #     if x == "ABC":
# #         sum = sum + x [2]
# #     else:
# #         continue 

# # number = (random.randint(1, 10)


# # guess = input("ENTER A GUESS: ")

 
# # if guess > number: 
# #     print ("number is too low ")
# #     if guess < number:
# #         print ("number is greater")

# # while  guess == guess:
# #     print ("congratulation you won ". upper())
# # def numberGuess():
# #     print("i'm thinking of a number between 1 to 10 ")
# # guess = 0 
# # randnum = random.randint(1, 10 )
# # print (randnum)
# # while guess != randnum:
# #     guess = int(input("try to guess a number : "))
# #     if (guess == randnum):
# #         print ("congratulation you won!!!!!!!!!!". upper())
# #         break
# #     if (guess < randnum):
# #         print ("the number is lower". upper())
# #         guess = int(input("try to guess a number : "))
# #     if (guess > randnum):
# #         print ("number is greater". upper())

# #  guessing game using random number

# secretnumber = random.randint(1,10)
# guess_count = 0 
# while guess_count < 5:
#     guess = int (input ("enter a guessing number: "))
#     if guess < secretnumber:
#         print ("number is lower".upper())
#         Beep(1000, 300)
#     if guess > secretnumber:
#         print( "number is greater".upper())
#         Beep(1000, 300)
#     if guess == secretnumber:
#         print("congratualtion you won !!!".upper())
#         break


# # # let ALL the box represent ABC
# # # let_our_c = 5 NUMBER OF ITEM 3
# # C = 555
# # AB = (C // 3)
# # message = (AB)
# # print(f"this is the result of our ABC {message}")

# # while True:

# #      input("GUESS NUMBER: ")

# #      GUESS_NUMBER = random.randint(1,10)
# #      if GUESS_NUMBER > 0:
# #          GUESS_NUMBER -= 1
# #          print("number is too low")
# #          if GUESS_NUMBER < 10:
# #              print ("number is greater")
# # else:
# #     print ("congratulation")






#     #  die2 = random.randint(1,6)

#     #  print ("DIE1-", die1)
#     #  print ("DIE2-", die2)

#     #  if die1 == die2 == 6:
#     #      print ("congratulations you got siki 2".upper())
#     #      break
#     #  else:
#     #     print ("sorry try again...!!!".upper())


# # TO GET THE NUMERICAL VALUES OF THE TRIANGLE WE ARE GOING TO TEST 0 T0 9
# # cause our xyz + xyz + xyz = zzz
# #  DIVINE BY NUMBER OF ITEM = 3
# # let skip 0,1,2,
# # let our xyz be = 000,111,222,333,444,555,666,777,888,999.
# # ITEM = 3

# # while True:
# #     VALUES = int( input ("ENTER ANY NUMBER FROM 3 TO 9 in three places: "))
# #     result = VALUES // ITEM
# #     print (result)
# #     if result 
# #     # answer = result + result + result 
# # a  = [3]
# # for i in ["1","8","5","1","8","5","1","8","5"]:
# #     if i == "5":
# #         a.append(i)
# #         print("".join (a))
# #         break



# def j(a,b,c):
#     x = 0 >= a and a >= 9
#     y = 0 >= a and a >= 9
#     z = 0 >= a and a >= 9
#     return x and y and z 
# def k (a,b,c):
#     return a * 300 + b * 30 + c * 3 == c*111 and j( a,b,c)
# answer = []
# a = 0
# b = 0
# c = 0
# while j (a,b,c):
#     if (a,b,c):
#         answer += [[a,b,c].copy ()]
#         c +=1
#     c = 0 
#     b +=0 
#     b = 0 
#     a+=1
# for x in answer :
#     s = 'f{x[0]}{x{[1]}{x[2]}+'*3
#     s = s [:-1]
#     s += 'f={x[2]}{x{[2}}{x[2]}+'*3
#     print (s)

    
