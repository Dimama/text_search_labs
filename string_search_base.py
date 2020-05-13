from typing import Iterable
from abc import abstractmethod


class StringSearchBase:
    @abstractmethod
    def search_pattern(self, string: str, pattern: str) -> Iterable[int]:
        """
        Search pattern in string and return positions of founded patterns,
        empty iterable if not found

        :param string: string in which search pattern
        :param pattern: pattern which need find
        :return: iterable with positions of founded pattern
        """
        raise NotImplementedError

    @staticmethod
    def check_data(string) -> None:
        if len(string) == 0:
            raise ValueError('Check string size!')

