# Backtracking 1: with list comprehension

def backtrack_comp(list, s):

    '''
        Usage:
            print(backtrack_comp(1, ["a","b","c"]))
            print(backtrack_comp(2, ["a","b","c"]))
        Output:
            ['a', 'b', 'c']
            ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    '''

    if list == 1:
        return s
    else:
        return [ x + y
                 for x in backtrack_comp(1, s)
                 for y in backtrack_comp(list - 1, s)
                 ]
