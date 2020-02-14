
import numpy as np

numbers_list = np.arange(1,10) ; print(f'\n{numbers_list}\n')

for i in range (len(numbers_list)):

    if i > 3 and i < 8:
        print(i*2,"\n")

