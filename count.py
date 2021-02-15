count=0
oddnum = 0
total_number=int(input("enter the max number you want to count"))
for i in range(1,total_number + 1):
    even =i%2
    if even==0:
        count +=1
        total_number-=1
    else:
            oddnum+=1

print(f"there are {count} even numbers and {oddnum} odd numbers")
print(oddnum)
    


