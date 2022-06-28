# guess 

import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count += 1
    pred = int(input('guess ')) 
    if pred > number:
        print('less')
    elif pred < number:
        print('more')
    else:
        print('yeah')
        break #real br 