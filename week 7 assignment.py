d = {'a': 1, 'b': 2}
d.update({'c': 3})
d['b'] = 3

c = {'a': [1, 3], 'b': [5, 7]}
c['a'].insert(1,2)

e = {'a': 1, 'c': 3, 'b': 2}

f = {'a': [1, 3], 'b': [5, 7, 9], 'c': [11]}

tup = (1,2,3)

g = {1: ['a', 'b', 'c'], 2: ['d', 'e'], 3: []}
l = []
for k in g:
    l.extend(g[k])
total = len(l)

L = [['apple', 3], ['pear', 2], ['banana', 3]]
z = {}
for item in L:
   z[item[0]] = item[1]


def contains(v, d):
    ''' (object, dict of {object: list}) -> bool

    Return whether v is an element of one of the list values in    d.
    >>> contains('moogah', {1: [70, 'blue'], 2: [1.24, 'moogah'    , 90], 3.14: [80, 100]})
    True
    >>> contains('moogah', {'moogah': [1.24, 'frooble', 90], 3.    14: [80, 100]})
    False
    '''

    found = False # Whether we have found v in a list in d.

    for k in d:
        if v in d[k]:
            found = True
 
    
