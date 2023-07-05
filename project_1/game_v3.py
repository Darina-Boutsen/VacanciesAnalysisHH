"""The game make a number and guess it itself"""

import numpy as np

def game_core_v3(number: int = np.random.randint(1, 101)) -> int:
    """
    Randomly guess a number
        The function takes a guessable number and returns the number of attempts.

    Args:
        number (int, optional): Guessable number.

    Returns:
        int: Number of attempts.
    """
    
    
    count = 0
    min_number = 0
    max_number = 100
    predict_number = np.random.randint(1, 101)
 
    while True:
        count += 1
        
        if predict_number > number:
            max_number = predict_number - 1
            predict_number = (max_number + min_number) // 2

        elif predict_number < number:
            min_number = predict_number + 1
            predict_number = (max_number + min_number) // 2
            
        else:
            break #end of the game

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