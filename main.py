from naive_search import NaiveSearch
from rabin_karp_search import RabinKarpSearch
from knuth_morris_pratt_search import KMPSearch
from boyer_moore_search import BoyerMooreSearch

if __name__ == '__main__':
    string = input('Enter string: ')
    pattern = input('Enter pattern to search: ')

    search_result = BoyerMooreSearch().search_pattern(string, pattern)
    print(search_result)
