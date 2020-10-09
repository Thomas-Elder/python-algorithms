
from timeit import default_timer as timer
from random import sample
import random

from algorithms.sort.insertion import insertion
from algorithms.sort.merge import merge
from algorithms.sort.bubble import bubble
from algorithms.sort.bubble import bubble_recursive
from algorithms.search.linear import linearSearch


# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable()

def unsortedList():
    a = []
    for i in range(1, 10000):
        logging.debug(i)
        a.append(random.randint(1, 20))

    return a

# Insertion sort
a = unsortedList()
start = timer()
insertion(a, order='ascending')
end = timer()

print(f'Insertion sort exection time: {round(end-start, 2)} seconds')

# Merge sort
a = unsortedList()
start = timer()
merge(a)
end = timer()

print(f'Merge sort exection time: {round(end-start, 2)} seconds')

# Bubble sort
a = unsortedList()
start = timer()
bubble(a)
end = timer()

print(f'Bubble sort exection time: {round(end-start, 2)} seconds')

# Bubble sort - recursive
a = unsortedList()
start = timer()
bubble_recursive(a)
end = timer()

print(f'Bubble sort exection time: {round(end-start, 2)} seconds')

# Linear search
a = unsortedList()
start = timer()
linearSearch(a, 100)
end = timer()

print(f'Linear search exection time: {round(end-start, 2)} seconds')