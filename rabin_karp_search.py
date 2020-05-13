from typing import Iterable

from string_search_base import StringSearchBase


class RabinKarpSearch(StringSearchBase):

    def __init__(self, d: int, q: int):
        """
        :param d: simple number for hash calculation
        :param q: alphabet size
        """
        self.d = d
        self.q = q

    def search_pattern(self, string, pattern) -> Iterable[int]:

        self.check_data(string)

        str_len = len(string)
        pattern_len = len(pattern)
        positions = []

        if pattern_len > str_len:
            return positions

        h = pow(self.d, pattern_len - 1) % self.q
        p_hash = 0
        s_hash = 0
        for i in range(pattern_len):
            p_hash = (self.d * p_hash + ord(pattern[i])) % self.q
            s_hash = (self.d * s_hash + ord(string[i])) % self.q
        for i in range(str_len - pattern_len + 1):
            if p_hash == s_hash and string[i:i+pattern_len] == pattern:
                positions.append(i)

            if i < str_len - pattern_len:
                s_hash = (s_hash - h * ord(string[i])) % self.q
                s_hash = (s_hash * self.d + ord(string[i + pattern_len])) % self.q
                s_hash = (s_hash + self.q) % self.q

        return positions
