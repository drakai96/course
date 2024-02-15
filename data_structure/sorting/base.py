from typing import List
from abc import ABC, abstractmethod


class BaseSort:
    @abstractmethod
    def sort(self, array: List[int]) -> List[int]:
        raise NotImplemented
