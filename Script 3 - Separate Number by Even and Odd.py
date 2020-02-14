# Script to create arrays of odd and even numbers
# extracted from an array of numbers from 1-9

import numpy as np

# Create the array of 1-9 numbers
num_list = np.arange(1,10); print(f'\n{num_list}\n')

#Create empty arrays to receive odd and even numbers
even_nums = np.empty(0); odd_nums = np.empty(0)

# For each number in the array, verify the mod 2 result
# and append to an array of odd or even numbers accordingly
for num in num_list:

    if num % 2 and num != 0:
        odd_nums=np.append(odd_nums, num)

    else:
        even_nums= np.append(even_nums, num)


print(f'{odd_nums}\n {even_nums}')

