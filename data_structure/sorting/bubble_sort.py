from typing import List
from base import BaseSort


class Bubble_Sort(BaseSort):
    def sort(self, array: List[int]) -> List[int]:
        for i in range(len(array)):
            for j in range(0, len(array)):
                if array[i] < array[j]:
                    array[i], array[j] = array[j], array[i]
        print("Array sorted: ", array)
        return array


if __name__ == "__main__":
    array = Bubble_Sort().sort([1, 3, 4, 5])
    # result
