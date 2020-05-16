from typing import List

from string_search_base import StringSearchBase


class BoyerMooreSearch(StringSearchBase):
    @staticmethod
    def _offsets(string: str) -> List[int]:
        offsets = [-1] * 256

        for i in range(len(string)):
            offsets[ord(string[i])] = i

        return offsets

    def search_pattern(self, string: str, pattern: str) -> List[int]:

        self.check_data(string)

        str_len = len(string)
        pattern_len = len(pattern)
        offsets = self._offsets(pattern)
        positions = []

        shift = 0
        while shift <= str_len - pattern_len:
            j = pattern_len - 1
            while j >= 0 and pattern[j] == string[shift + j]:
                j -= 1

            if j < 0:
                positions.append(shift)
                if shift + pattern_len < str_len:
                    shift += pattern_len - offsets[ord(string[shift + pattern_len])]
                else:
                    shift += 1
            else:
                shift += max(1, j - offsets[ord(string[shift + j])])

        return positions
