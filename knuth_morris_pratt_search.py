from typing import List

from string_search_base import StringSearchBase


class KMPSearch(StringSearchBase):
    @staticmethod
    def _prefix(string: str) -> List[int]:
        prefix = [0]*len(string)
        for i in range(1, len(string)):
            j = prefix[i-1]
            while j > 0 and string[j] != string[i]:
                j = prefix[j-1]
            if string[j] == string[i]:
                j += 1
            prefix[i] = j
        return prefix

    def search_pattern(self, string: str, pattern: str) -> List[int]:

        self.check_data(string)

        str_len = len(string)
        pattern_len = len(pattern)
        positions = []
        prefix = self._prefix(string)

        j = 0
        for i in range(str_len):
            while j > 0 and string[i] != pattern[j]:
                j = prefix[j-1]
            if string[i] == pattern[j]:
                j += 1
            if j == pattern_len:
                positions.append(i - pattern_len + 1)
                j = prefix[j-1]

        return positions
