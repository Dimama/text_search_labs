from typing import Iterable

from string_search_base import StringSearchBase


class NaiveSearch(StringSearchBase):
    def search_pattern(self, string, pattern) -> Iterable[int]:

        self.check_data(string)

        str_len = len(string)
        pattern_len = len(pattern)
        positions = []

        if pattern_len > str_len:
            return positions

        for i in range(str_len - pattern_len + 1):
            j = 0
            for k in range(pattern_len):
                if string[i + k] != pattern[k]:
                    break
                j += 1

            if j == pattern_len:
                positions.append(i)

        return positions
