
import sys

def fibonacci (n: int) -> int:
    '''
    Recursively solves for the nth number in the fibonacci sequence.
    Don't run for large numbers! Python doesn't like recursion.

    Limit case is n == 1, the function makes recursive calls tending
    to this limit and returns their value. 

    Parameters
    ----------
    n: the index in the fibonacci sequence

    Returns
    -------
    ??? More fibonacci calls until n == 1
    '''

    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    print(fibonacci(int(sys.argv[1])))