"""The game make a number and guess it itself"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    First we create list (from 1 to 100), then we search middle element of our list.
    If the guessable number is not the middle number, we will search in left or right parts of our list
    depending on less or more the guessable number than our mibble number.
    Then we search a new middle number in chosen part and repeat the algorithm.
        The function takes a guessable number and returns the number of attempts.

    Args:
        number (int, optional): Guessable number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    
    count = 1
    a = range(1, 101)
 
    mid = len(a) // 2
    low = 0
    high = len(a) - 1
 
    while a[mid] != number and low <= high:
        count += 1
        if number > a[mid]:
            low = mid + 1
            count += 1
        else:
            high = mid - 1
            count += 1
        mid = (low + high) // 2

    # Output the result
    return count


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
    score_game(game_core_v3)