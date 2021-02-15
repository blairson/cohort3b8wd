import random 
from winsound import Beep

secretnumber = random.randint(1,10)
guess_count = 0 
while guess_count < 5:
    guess = int (input ("guess number FROM 1 TO 10 : "))
    if guess < secretnumber:
        print ("number is lower".upper())
        Beep(1000, 300)
    elif guess > secretnumber:
        print( "number is greater".upper())
        Beep(1000, 300)
    elif guess == secretnumber:
        print("congratualtion you won !!!".upper())
        break
    else:
        print('keep guessimg'.upper())
        