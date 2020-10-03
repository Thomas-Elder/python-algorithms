
from timeit import default_timer as timer
from random import sample

from algorithms.sort import insertion

# logging
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

a = sample(range(1, 100000), 10000)
sorter = insertion.Insertion()

# time execution
start = timer()
sorter.sort(a)
end = timer()

logging.info(f'Exection time: {round(end-start, 2)} seconds')