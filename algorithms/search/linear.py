
def linearSearch(a: list, v: int) -> int:
    '''Returns the index of the value v, in list a 

    If v is not found in a, then -1 is returned.

    Parameters
    ----------
    a: a list of integers
    v: an integer

    Returns
    -------
    The index of value v in list a
    '''
    
    for j in range(len(a)):
        if a[j] == v:
            return j

    return -1