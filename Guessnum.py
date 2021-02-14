#ASSIGNMENT
#GUESSING GAME 

import random
from winsound import Beep
rand= random.randint(1,100)
guess = 10

while guess > 0:
    guess -=1
    rand_entry=int (input (f"Guess a numBer from 1-100.   n/you have {guess} guesses left: "))
    if rand_entry==rand:
        print("CONGRATULATIONS  YOU JUST WON A MILLION NAIRA")
        Beep (400, 200)
        break

    elif abs(rand - rand_entry) <=10:
        print("You are almost there...... Try again ")
        continue
    
    elif rand_entry - rand > 10:
        print("the entry is higher than")
        continue

    elif rand_entry - rand <10:
        print("KEEP TRYING YOU WILL GET IT. ")
else:
    print("you have reached the maximum number of guesses::::::::")
    print("PLEASE PAY TO ACCESS ANOTHER GUESS")


