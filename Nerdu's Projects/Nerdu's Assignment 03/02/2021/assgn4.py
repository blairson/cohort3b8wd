#Name and Last Name
fname = input("Enter your first name please: ")  
sname = input("Enter your second name: ")
fe = open(f"{sname}.txt", "w")
fe.write(f"{fname}")
print ("Your file has been saved.")