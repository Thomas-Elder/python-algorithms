
def selection(a: list, order: str) -> list:

    if order == 'ascending':

        for i in range(len(a)): 
        
            # Find the minimum element in remaining  
            # unsorted array 
            min_idx = i 
            for j in range(i+1, len(a)): 
                if a[min_idx] > a[j]: 
                    min_idx = j 
                    
            # Swap the found minimum element with  
            # the first element         
            a[i], a[min_idx] = a[min_idx], a[i]

    else:

        for i in range(len(a)): 
        
            # Find the minimum element in remaining  
            # unsorted array 
            max_idx = i 
            for j in range(i+1, len(a)): 
                if a[max_idx] < a[j]: 
                    max_idx = j 
                    
            # Swap the found minimum element with  
            # the first element         
            a[i], a[max_idx] = a[max_idx], a[i]

    return a