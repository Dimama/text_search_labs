from typing import List

from string_search_base import StringSearchBase


class BoyerMooreSearch(StringSearchBase):
    def search_pattern(self, string: str, pattern: str) -> List[int]:

        self.check_data(string)

        str_len = len(string)
        pattern_len = len(pattern)
        positions = []


        return positions
