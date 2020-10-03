
from timeit import default_timer as timer
from random import sample

from algorithms.sort.insertion import insertion
from algorithms.search.linear import linearSearch

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

a = sample(range(1, 100000), 10000)

start = timer()
insertion(a, order='ascending')
end = timer()

logging.info(f'Exection time: {round(end-start, 2)} seconds')

a = sample(range(1, 100000), 10000)

start = timer()
linearSearch(a, 100)
end = timer()

logging.info(f'Exection time: {round(end-start, 2)} seconds')