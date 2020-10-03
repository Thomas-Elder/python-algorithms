
class LinearSearch:

    def __init__(self):
        pass

    def find(self, a: list, v: int) -> int:

        for j in range(len(a)):
            if a[j] == v:
                return j

        return -1