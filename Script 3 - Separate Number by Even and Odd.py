
import numpy as np

num_list = np.arange(1,10); print(f'\n{num_list}\n')

even_nums = np.empty(0); odd_nums = np.empty(0)

for num in num_list:

    if num % 2 and num != 0:
        odd_nums=np.append(odd_nums, num)

    else:
        even_nums= np.append(even_nums, num)

print(f'{odd_nums}\n {even_nums}')

