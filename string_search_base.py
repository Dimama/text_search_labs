from typing import Iterable
from abc import abstractmethod


class StringSearchBase:
    def __init__(self, string: str, pattern: str):
        if len(string) == 0:
            raise ValueError('String can"t be empty!')
        self.string = string
        self.pattern = pattern

    @abstractmethod
    def search_pattern(self) -> Iterable[int]:
        """
        Search pattern in string and return positions of founded patterns,
        empty iterable if not found

        :return: iterable with positions of founded pattern
        """
        raise NotImplementedError
