
def merge(a: list) -> list:
    '''Sorts the list a in ascending order by default

    Parameters
    ----------
    a: a list of integers
    order: a string, can be ascending or descending

    Returns
    -------
    A list of sorted integers
    '''

    if len(a) > 1:
        mid = len(a) // 2
        L = a[:mid] 
        R = a[mid:]
  
        merge(L) 
        merge(R)
  
        i = j = k = 0
          
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                a[k] = L[i] 
                i += 1
            else: 
                a[k] = R[j]
                j += 1
            k += 1
          
        while i < len(L): 
            a[k] = L[i] 
            i += 1
            k += 1
          
        while j < len(R): 
            a[k] = R[j] 
            j += 1
            k += 1

    return a