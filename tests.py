import inject

from string_search_base import StringSearchBase
from naive_search import NaiveSearch
from rabin_karp_search import RabinKarpSearch
from knuth_morris_pratt_search import KMPSearch
from boyer_moore_search import BoyerMooreSearch


# inject search class realization
def config(binder):
    binder.bind_to_constructor(StringSearchBase, lambda: BoyerMooreSearch())


inject.configure(config)


@inject.params(searcher=StringSearchBase)
def test_simple_not_found(searcher: StringSearchBase = None):
    string = 'abcedf'
    pattern = 'hjk'

    assert searcher.search_pattern(string, pattern) == []


@inject.params(searcher=StringSearchBase)
def test_pattern_equal_string(searcher: StringSearchBase = None):
    string = 'string'
    pattern = 'string'

    assert searcher.search_pattern(string, pattern) == [0]


@inject.params(searcher=StringSearchBase)
def test_string_consist_of_patterns(searcher: StringSearchBase = None):
    string = 'aaaaaaa'
    pattern = 'a'

    assert searcher.search_pattern(string, pattern) == [0, 1, 2, 3, 4, 5, 6]


@inject.params(searcher=StringSearchBase)
def test_string_consist_of_double_pattern(searcher: StringSearchBase = None):
    string = 'python python '
    pattern = 'python '

    assert searcher.search_pattern(string, pattern) == [0, 7]


@inject.params(searcher=StringSearchBase)
def test_many_random_positions(searcher: StringSearchBase = None):
    string = '123567829230123042598238923'
    pattern = '23'

    assert searcher.search_pattern(string, pattern) == [1, 9, 13, 21, 25]


@inject.params(searcher=StringSearchBase)
def test_minimal_equal_pattern_and_string(searcher: StringSearchBase = None):
    string = '@'
    pattern = '@'

    assert searcher.search_pattern(string, pattern) == [0]


@inject.params(searcher=StringSearchBase)
def test_minimal_not_equal_pattern_and_string(searcher: StringSearchBase = None):
    string = '#'
    pattern = '@'

    assert searcher.search_pattern(string, pattern) == []
