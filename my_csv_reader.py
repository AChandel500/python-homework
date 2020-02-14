# Script to read and print the 'housing.data' file
# and to convert each line to a list

import os
import numpy as np

#Set the path variable to the file location
path= "/home/user/PycharmProjects/python-homework/housing.data"

# Use OS library functions to assess if path is a file or directory
if os.path.isdir(path):
    print("Boo no file for me.\n")
if os.path.isfile(path):
    print("I have a file to process\n")

# Open path and print contents line by line
with open(path, 'r') as f:

    line = f.readline()
    while (line != ''):
        print(line)
        line = f.readline()

# Load path into numpy array to print as list
housing_data = np.genfromtxt(path)
max_rows = housing_data.shape[0]

for i in range (0, max_rows):
    print(list(housing_data[i][:]))
    i+=1
