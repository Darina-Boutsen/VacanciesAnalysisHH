"""The game - guess the number"""

import numpy as np

number = np.random.randint(1, 101) # make the number

# number og attempts
count = 0

while True:
    count += 1
    predict_number = int(input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The number must be less")
    elif predict_number < number:
        print("The number must be more")
    else:
        print(f"You guessed the number in {count} attempts! This is {number}.")
        break # the game end

