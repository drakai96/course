from typing import List
from base import BaseSort


class SelectionSort(BaseSort):
    def sort(self, array: List[int]) -> List[int]:
        new_array = array
        for i in range(len(new_array)):
            compare_array = new_array[i:]
            min_value, idx_min = self.min_function(compare_array)
            idx_min += i
            new_array[i] = min_value
            new_array[idx_min] = compare_array[0]
        print(new_array)
        return new_array

    def min_function(self, array):
        min_value = array[0]
        idx_min = 0
        for idx, value in enumerate(array):
            if value < min_value:
                min_value = value
                idx_min = idx
        return min_value, idx_min


if __name__ == "__main__":
    array = SelectionSort().sort([2, 4, 56, 2, 5, 43, 2, 9, 2, 5, 23, 10])
