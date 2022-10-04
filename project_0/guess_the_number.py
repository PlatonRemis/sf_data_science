import random
import math

def random_number():
    """ This function simply generates a random
        number from 1 to 100

    Returns:
        int: in range from 1 to 100
        including the end point
    """
    return random.randint(1, 100)

def guess(number) -> int:
    """ This function will try to guess given number
        in as few attempts as possible

    Args:
        number (int): function takes the number
        it tries to guess as an argument
        
    Returns:
        count (int): returns number of guesses it took
        to find the number
    """
    
    count = 0 # This value keeps track of guess attempts
    
    current = 50 # This value we will compare to the number we try to guess
    
    step = 50 # This is the amount we will add or substract to our current value
    
    while True:
        step = math.ceil( step / 2 )
        # With each attempt we make even smaller steps
        # rounding up so we won't get 0 thus get stuck
        
        count += 1
        
        if current == number:
            return count
        
        if number > current:
            current += step
            
        if number < current:
            current -= step
            
            
                  
