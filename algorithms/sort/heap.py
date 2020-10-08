
def heapify(a, n, i, order='ascending'): 

    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 

    if order == 'ascending':
        # See if left child of root exists and is 
        # greater than root 
        if l < n and a[i] < a[l]: 
            largest = l 
    
        # See if right child of root exists and is 
        # greater than root 
        if r < n and a[largest] < a[r]: 
            largest = r 
    
        # Change root, if needed 
        if largest != i: 
            a[i],a[largest] = a[largest],a[i] # swap 
    
            # Heapify the root. 
            heapify(a, n, largest) 

    else: 
        smallest = i

        # See if left child of root exists and is 
        # smaller than root 
        if l > n and a[i] > a[l]: 
            smallest = l 
    
        # See if right child of root exists and is 
        # smaller than root 
        if r > n and a[smallest] > a[r]: 
            smallest = r 
    
        # Change root, if needed 
        if smallest != i: 
            a[i],a[smallest] = a[smallest],a[i] # swap 
    
            # Heapify the root. 
            heapify(a, n, smallest) 

# The main function to sort an array of given size 
def heap(a, order='ascending'): 

    n = len(a) 
  
    if order == 'ascending':
        # Build a maxheap. 
        for i in range(n//2 - 1, -1, -1): 
            heapify(a, n, i) 
    
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            a[i], a[0] = a[0], a[i] # swap 
            heapify(a, i, 0, order='ascending') 
        
    else:

        # Build a maxheap. 
        for i in range(n//2 - 1, -1, -1): 
            heapify(a, n, i) 
    
        # One by one extract elements 
        for i in range(n-1, 0, -1): 
            a[i], a[0] = a[0], a[i] # swap 
            heapify(a, i, 0, order='descending') 
    
    return a