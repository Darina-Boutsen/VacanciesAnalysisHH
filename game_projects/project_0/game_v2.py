"""The game make a number and guess it itself"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Guess a random number

    Args:
        nunber (int, optional): predict number. Defaults to 1.

    Returns:
        int: the number of attempts
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Make the number
        if number == predict_number:
            break #The end of the cycle
    return count

print(f"The number of attemts is {random_predict()}")


def score_game(random_predict) -> int:
    """The average number of attemts to guess the number for 1000 approaches

    Args:
        random_predict (_type_): the function to guess

    Returns:
        int: the average number of attemts
    """
    
    count_ls = [] # The list of attempts
    np.random.seed(1) # The seed for random making
    random_array = np.random.randint(1, 101, size=(1000)) # Make the list of numbers
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # Find the averade
    print(f"Your algorithm guess the number in average of {score} attempts.")
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)