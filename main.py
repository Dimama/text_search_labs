from naive_search import NaiveSearch
from rabin_karp_search import RabinKarpSearch

if __name__ == '__main__':
    string = input('Enter string: ')
    pattern = input('Enter pattern to search: ')

    search_result = RabinKarpSearch(7219, 256).search_pattern(string, pattern)
    print(search_result)
