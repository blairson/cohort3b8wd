# n = 1
# while n < 13:
#     multn = 2 * n
#     print (f"2 x {n} | {multn}")
#     n += 1
    
# principal = int(input("Please enter the borrowed amount: ")) 
# time = int(input("Please enter the duration of loan (in months): ")) 
# rate = int(input("Please enter the rate of interest: : ")) 
# interest = principal * rate * time * 0.01
# amount = principal + (interest)
# monthly = amount / time

# print ("Here is your payment schedule: ")
# n = 1
# while n <= time:
#     print (f"Month {n} - N{monthly}")
#     n += 1


# for i in range (1, 9):
#     for n in range (1, 4):
#         print (f"{n*i}".center(5), "|", end = "")
#     print()
#     print ("-"*21)
    


end_number = int(input("Enter end number: "))
count = 0
oddcount = 0

for i in range (1, end_number + 1):
    even = i % 2
    if even ==0:
      count += 1
      
      end_number -= 1
    else:
      oddcount += 1

    
print (f"There are {count} even numbers and {oddcount} odd numbers.")

    