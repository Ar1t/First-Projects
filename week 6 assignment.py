def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is         this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

mystery('civil')

def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)


def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

def shift_right(L):
    
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''
    
    last_item = L[-1]
    L = ['a','b','c','d']
    for i in range(1, len(L)):
        L[len(L)- i] = L[len(L)-i-1]
    L[0] = last_item
ans = shift_right(['a','b','c','d'])
print(ans)


numbers = [[1,2,3],[4,5,6],[7,8,9]]
x = numbers[2][0]
print(x)

for i in range(2, 5):
    for j in range(4, 9):
        print(i, j)


def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False  # We have not yet found value in the list.

    for item in lst:
        if value == list:
            value = True 
    return found
y = contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
print(y)


def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False  # We have not yet found value in the list.

    for sublist in lst:
        if value in sublist:
            found = True 
    return found
z = contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
print(z)


def contains(value, lst):
    """ (object, list of list) -> bool
  
   Return whether value is an element of one of the nested        lists in lst.

   >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
   True
   """

    found = False  # We have not yet found value in the list.

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
    return found
q = contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
print(q)