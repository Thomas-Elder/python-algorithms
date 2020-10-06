
from timeit import default_timer as timer
from random import sample

from algorithms.sort.insertion import insertion
from algorithms.sort.merge import merge
from algorithms.sort.bubble import bubble
from algorithms.search.linear import linearSearch

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

x, y = 100000, 10000

# Insertion sort
a = sample(range(1, x), y)
start = timer()
insertion(a, order='ascending')
end = timer()

print(f'Insertion sort exection time: {round(end-start, 2)} seconds')

# Merge sort
a = sample(range(1, x), y)
start = timer()
merge(a)
end = timer()

print(f'Merge sort exection time: {round(end-start, 2)} seconds')

# Merge sort
a = sample(range(1, x), y)
start = timer()
bubble(a)
end = timer()

print(f'Bubble sort exection time: {round(end-start, 2)} seconds')

# Linear search
a = sample(range(1, x), y)
start = timer()
linearSearch(a, 100)
end = timer()

print(f'Linear search exection time: {round(end-start, 2)} seconds')
