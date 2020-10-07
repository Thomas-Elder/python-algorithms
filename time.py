
from timeit import default_timer as timer
from random import sample
import random

from algorithms.sort.insertion import insertion
from algorithms.sort.merge import merge
from algorithms.sort.bubble import bubble
from algorithms.search.linear import linearSearch


# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def unsortedList():
    a = []
    for i in range(1, 1000):
        a.append(random.randint(1, 20))

    return a

# Insertion sort
a = unsortedList()
print(f'Unsorted list:')
print(a)

start = timer()
insertion(a, order='ascending')
end = timer()

print(f'Insertion sort exection time: {round(end-start, 2)} seconds')
print(f'Sorted list:')
print(a)

# Merge sort
a = unsortedList()
print(f'Unsorted list:')
print(a)

start = timer()
merge(a)
end = timer()

print(f'Merge sort exection time: {round(end-start, 2)} seconds')
print(f'Sorted list:')
print(a)

# Bubble sort
a = unsortedList()
print(f'Unsorted list:')
print(a)

start = timer()
bubble(a)
end = timer()

print(f'Bubble sort exection time: {round(end-start, 2)} seconds')
print(f'Sorted list:')
print(a)

# Linear search
a = unsortedList()
print(f'Unsorted list:')
print(a)

start = timer()
linearSearch(a, 100)
end = timer()

print(f'Linear search exection time: {round(end-start, 2)} seconds')
print(f'Sorted list:')
print(a)