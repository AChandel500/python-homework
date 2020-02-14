# Print integers from 1-100
# For multiples of 3, print 'Fizz' instead
# For multiples of 5, print 'Buzz' instead
# For multiples of both 3 and 5, print 'FizzBuzz' instead

for i in range(1,101):

    if (i % 3 == 0) and (i % 5 == 0):
        print(f'FizzBuzz\n')
        continue
    elif (i % 3 == 0):
        print("Fizz\n")
    elif (i % 5 == 0):
        print("Buzz\n")
    else:
        print(f'{i}\n')
