
class Insertion:

    def __init__(self):
        pass

    def sort(self, a: list) -> list:

        for j in range(1, len(a)): 
            key = a[j]
            i = j - 1

            # shuffle everything to the right, while a[i] is > key
            while i >= 0 and a[i] > key:
                a[i + 1] = a[i]
                i = i - 1
            
            a[i + 1] = key

        return a