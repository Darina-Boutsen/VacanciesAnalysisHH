"""The game make a number and guess it itself"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    First we get a random number, then we determine in what quater of the number 100 is the number.
    Then we create new random number in this quater and increase or decrease it depending on
    wheather it is more or less than the specified one.
        The function takes a guessable number and returns the number of attempts.

    Args:
        number (int, optional): Guessable number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    
    count = 0
    predict = np.random.randint(1, 101)

    while number != predict:
        count += 1
        if number > 50:
            if number > 75:
                predict = np.random.randint(76, 101)
                if number > predict:
                    predict += 1
                elif number < predict:
                    predict -= 1
            else:
                predict = np.random.randint(51, 76)
                if number > predict:
                    predict += 1
                elif number < predict:
                    predict -= 1
        else:
            if number < 25:
                predict = np.random.randint(1, 26)
                if number > predict:
                    predict += 1
                elif number < predict:
                    predict -= 1
            else:
                predict = np.random.randint(26, 50) 
                if number > predict:
                    predict += 1
                elif number < predict:
                    predict -= 1

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