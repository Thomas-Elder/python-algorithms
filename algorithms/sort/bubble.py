
def bubble(a: list, order='ascending') -> list:
    n = len(a)

    if order == 'ascending':
        
        # traverse all elements
        for i in range(n - 1):

            # last i elements are sorted
            for j in range(n - i - 1):

                # traverse array from 0 to n - i - 1
                # swap element if it's greater 
                # than the next element
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

    else: 

        # traverse all elements
        for i in range(n - 1):

            # last i elements are sorted
            for j in range(n - i - 1):

                # traverse array from 0 to n - i - 1
                # swap element if it's greater 
                # than the next element
                if a[j] < a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

    return a

def bubble_recursive(a: list) -> list:

    for i, num in enumerate(a):
        
        # avoid index out of bounds, check i+1 is valid
        if i + 1 < len(a):
            
            # if the next element is less than the current one, swap em
            if a[i + 1] < num:
                a[i] = a[i + 1]
                a[i + 1] = num

                bubble_recursive(a)
    
    return a