def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
          result = result + s[i]
          i = i + 1

    return result
x =mystery('123abc')
print(x)

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements       from Lconcatenated together, starting with indices 0 and 1,    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """ 
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2

    return compressed_list
y = compress_list(['a', 'b', 'c', 'd'])
print(y)




# using a while loop
i = 524
odd_sum = 0
while i <= 10508:
    odd_sum += i
    i += 2
print(odd_sum)

def while_version(L):
    """ (list of number) -> number
    """
    i = 0
    total = 0

    while i < len(L) and L[i] % 2 != 0:
        total = total + L[i]
        i = i + 1

    return total
z = while_version([1, 3, 7, 9, 11, 13, 17])
print(z)

def for_version(L):
    found_even = False
    total = 0
    for num in L:
        if num % 2 != 0:
            total = total + num
        elif not found_even:
            found_even = True
    return total
w = for_version([1, 3, 7, 9, 11, 13, 17])
print(w)

letters = ['b', 'd', 'a']
letters.sort()
print(letters)


veggies = ['carrot', 'broccoli', 'potato', 'asparagus']
veggies.insert(veggies.index('broccoli'), 'celery')
print(veggies)


a = [1, 2, 3]
b = [1, 2, 3]
a[1] = 'A'
print(a, b)

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)



values = []
for num in range(1,3):
    values.append(num*3)
print(values)


def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result
e = example([1, 2, 3, 4, 5, 6, 7])
print(e)

fruits = ['banana', 'apple', 'pear', 'peach']
fruits.insert(fruits.index('pear'), 'watermelon')
print(fruits)

a = [1, 2, 3]
b = a
b[1] = 'AB'
a[1] = a[1][0]


print(a, b)

values = []
for num in range(3,10,3):
    values.append(num)
print(values)

values = []
for num in range(1,4):
    values.append(num*3)
print(values)

