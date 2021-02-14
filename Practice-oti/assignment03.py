import random
computers_guess = random.randint ( 1, 20)
number_of_guess = 0
max_guess = 7


while number_of_guess<max_guess:
    guess = int(input("Enter your guess :"))
    number_of_guess +=1
    if guess == computers_guess:
        print(" you got the guess right")
        break
    elif guess < computers_guess:
        print ("too low")
    elif guess == computers_guess+1:
        print (" very close : too high by +1")
    elif guess == computers_guess-1:
        print ( "very close - too little by -1 ")
    elif guess > computers_guess:
        print ("too high")
else:
    print (" you have used all your guesses : ")
   
