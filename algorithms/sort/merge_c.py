
def mergeSort(arr, start, end):

        if start < end:
            mid = start + (end - l) // 2

            mergeSort(arr, start, mid)
            mergeSort(arr, mid + 1, end)

            merge(arr, start, mid, end)
    
    return arr

def merge(arr, start, mid, end):

    return arr