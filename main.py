from naive_search import NaiveSearch

if __name__ == '__main__':
    string = input('Enter string: ')
    pattern = input('Enter pattern to search: ')

    search_result = NaiveSearch().search_pattern(string, pattern)
    print(search_result)
