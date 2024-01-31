import random
import math

#inputs
lower = 0
upper = 25
 
# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tyou have 5 chances to guess a number between 0 and 20!\n")
 
# Initializing the number of guesses.
count = 0
 
# for calculation of minimum number of
# guesses depends upon range
while count < 5:
    count += 1
 
    # taking guessing number as input
    guess = int(input("guess a number:  "))
 
    # Condition testing
    if x == guess:
        print("you won")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("too small!")
    elif x < guess:
        print("too high!")
 
# If Guessing is more than required guesses,
# shows this output.
if count >= 5:
    print("\nthe number was %d" % x)