
def heapify(a, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
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
  
# The main function to sort an array of given size 
def heap(a): 
    n = len(a) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(a, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        a[i], a[0] = a[0], a[i] # swap 
        heapify(a, i, 0) 

    return a