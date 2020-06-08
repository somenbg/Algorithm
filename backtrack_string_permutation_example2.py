# Backtracking 2: with traditional for loops

def backtrack_trad(list, s):

    '''
        Usage:
            print(backtrack_trad(1, ["a","b","c"]))
            print(backtrack_trad(2, ["a","b","c"]))
        Output:
            ['a', 'b', 'c']
            ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    '''

    if list == 1:
        return s
    else:
        hold = []
        for x in backtrack_trad(1, ["a","b","c"]):
            for y in backtrack_trad(list - 1, ["a","b","c"]):
#                 print(x+y, end=" ")
                hold.append(x+y)
        return hold
    