from typing import List
from base import BaseSort


class InsertSort(BaseSort):
    def sort(self, array: List[int]) -> List[int]:
        for i in range(0, len(array)):
            for j in range(i, len(array)):
                if array[i] > array[j]:
                    array = array[:i] + [array[j]] + array[i:j] + array[j + 1 :]
        print("array sorted: ", array)
        return array


if __name__ == "__main__":
    array = InsertSort().sort([1, 2, 4, 5, 4, 2, 4, 5, 7, 1, 4, 1, 13])
    # array sorted:  [1, 1, 1, 2, 2, 4, 4, 4, 4, 5, 5, 7, 13]
