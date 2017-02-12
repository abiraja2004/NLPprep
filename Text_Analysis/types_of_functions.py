# function with single argument
def square(numbers):
    return numbers*numbers

square(55)

import numpy as np
np.square(44)

def squares(*args):
    squared_args = []
    for item in args:
        squared_args.append(item*item)
    return squared_args

squares(1, 2, 3, 4)

def person_details(**kwargs):
    for key, value in kwargs.items():
        print (key, '->', value)

person_details(name='James Bond', alias='007', job='Secret RAW Agent')

# simple lambda functions to square a number

lambda_square = lambda n : n*n

lambda_square(55)

# map function to find the even numbers used for filtering
lambda_evens = lambda n : n%2 == 0
lt_evens = list(filter(lambda_evens, [1, 2, 3, 4]))
print(lt_evens)

import functools as ft
lambda_sum = lambda x, y : (x + y)
print(list(ft.reduce(lambda_sum, [1, 2, 3, 4])))

lambda_sent_maker = lambda word1, word2 : ' '.join([word1, word2])

(ft.reduce(lambda_sent_maker, ['I', 'am', 'Pranav', 'Kanade']))

# iterators
# iterator object
numbers = [1, 2, 3, 4, 5]
iterator_obj = iter(numbers)

while True:
    try:
        print(iterator_obj.__next__())
    except StopIteration:
        print("EOS")
        break

print(type(range(10)))

# comprehensions
numbers = range(10)

# chk if no is divisible by 2
lt_ven = [num % 2 for num in numbers]
print(set(lt_ven))

st_sqr = {num : num * num
          for num in numbers}
print(st_sqr)
