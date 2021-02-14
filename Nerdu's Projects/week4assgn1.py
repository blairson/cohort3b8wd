import random
from winsound import Beep
myran = random.randint(1, 100)
guesses = 5

while guesses>0:
    guesses -= 1
    their_ran = int (input (f"Make a guess from 1 - 100. You have just {guesses} guesses left:  "))
    if myran==their_ran:
        print ("Congratulations! You guessed my number!")
        Beep (2000, 1000)
        break
    elif abs(myran - their_ran) <= 5:
        print ("You're so close! Try again.")
        continue
    elif their_ran-myran > 5: 
        print ("Reduce your guess. ")
        continue
    elif their_ran - myran < 5:
        print ("You're too low. Increase your guess. ")
else:
    print ("You have run out of guesses. Please try again.")



