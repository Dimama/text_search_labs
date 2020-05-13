from typing import Iterable

from string_search_base import StringSearchBase


class NaiveSearch(StringSearchBase):
    def search_pattern(self) -> Iterable[int]:

        str_len = len(self.string)
        pattern_len = len(self.pattern)
        positions = []

        if pattern_len > str_len:
            return positions

        for i in range(str_len - pattern_len + 1):
            j = 0
            for k in range(pattern_len):
                if self.string[i + k] != self.pattern[k]:
                    break
                j += 1

            if j == pattern_len:
                positions.append(i)

        return positions

