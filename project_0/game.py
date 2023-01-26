'''Game guess the number by computer !!!'''


import numpy as np


def random_predict(number: int = 1) -> int:
    """Randomly crack the number

    Args:
        number (int): Given number
        
    Returns:
        int: Number of attemps
    """
    count = 0
    min_num = 1
    max_num = 100 # Setting the limits of the selection of the number
    
    while True:
        count += 1
        predict_number = np.random.randint(min_num, max_num + 1)
        
        if predict_number > number: # Search condition for a new number
            max_num = predict_number
        elif predict_number < number:
            min_num = predict_number
        else:
            break # Exit the loop if guessed right
    return count


def score_games(random_predict) -> int:
    """Average number of 1000 attemps

    Args:
        random_predict ([type]): Guessing function
        
    Returns:
        int: Average number of attemps
    """
    count_lst = []
    np.random.seed(1) # Fix it for reproducibility
    random_array = np.random.randint(1, 101, size=1000) # Made a list of numbers
    
    for number in random_array:
        count_lst.append(random_predict(number))
        
    score = int(np.mean(count_lst))
    print(f'On average we guess the number in {score} attemps')
    return score

    
if __name__ == '__main__':
    # Run 
    score_games(random_predict)
