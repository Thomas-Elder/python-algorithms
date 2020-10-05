
from timeit import default_timer as timer
from random import sample

from algorithms.sort.insertion import insertion
from algorithms.sort.merge import merge
from algorithms.search.linear import linearSearch

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Insertion sort
a = sample(range(1, 10000000), 1000000)
start = timer()
insertion(a, order='ascending')
end = timer()

print(f'Insertion sort exection time: {round(end-start, 2)} seconds')

# Merge sort
a = sample(range(1, 10000000), 1000000)
start = timer()
merge(a)
end = timer()

print(f'Merge sort exection time: {round(end-start, 2)} seconds')

# Linear search
a = sample(range(1, 10000000), 1000000)
start = timer()
linearSearch(a, 100)
end = timer()

print(f'Linear search exection time: {round(end-start, 2)} seconds')
