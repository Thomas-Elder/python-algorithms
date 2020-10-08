
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
