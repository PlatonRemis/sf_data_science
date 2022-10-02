import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    predict_number = int(input('Guess a number form 1 to 100'))
    
    if predict_number > number:
        print('The number is less than that')
        
    elif predict_number < number:
        print('Number is bigger than that')
        
    else:
        print(f'You guessed the number in {count} guesses! It is {number}')
        break