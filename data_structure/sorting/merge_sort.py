from typing import List
from base import BaseSort


class MergeSort(BaseSort):
    def sort(self, array: List[int]) -> List[int]:
        if len(array) > 1:
            midle = len(array) // 2
            left_array = array[:midle]
            right_array = array[midle:]
            left_array = self.sort(left_array)
            right_array = self.sort(right_array)
            i = j = k = 0
            while i < len(left_array) and j < len(right_array):
                if left_array[i] < right_array[j]:
                    array[k] = left_array[i]
                    i += 1
                else:
                    array[k] = right_array[j]
                    j += 1
                k += 1
            if i < len(left_array):
                array[k:] = left_array[i:]
            if j < len(right_array):
                array[k] = right_array[j]
        return array


if __name__ == "__main__":
    array = MergeSort().sort([2, 3, 1, 34, 4, 32, 1, 4, 5])
    print("array sorted: ", array)
    # array sorted:  [1, 1, 2, 3, 4, 4, 5, 32, 34]
