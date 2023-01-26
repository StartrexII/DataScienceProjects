import numpy as np
'''game guess the number
by computer !!!'''


def random_predict(number):
    """randomly crack the number

    Args:
        number (int): given number
    """
    count = 0 
    while True:
        count += 1
        predict_number = np.random.randint(1,101)
        if number == predict_number:
            break
    return count


def score_games(random_predict):
    """Average number of 1000 attemps

    Args:
        random_predict (): Guessing function
    """
    count_lst = []
    np.random.seed(1) # fix it for reproducibility
    random_array = np.random.randint(1,101, size=1000) #made a list of numbers
    for number in random_array:
        count_lst.append(random_predict(number))
    score = np.mean(count_lst)
    print(f'On average we guess the number in {round(score)} attemps')
    return round(score)
    
if __name__ == '__main__':
# Run 
    score_games(random_predict)
