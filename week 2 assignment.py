def count_vowels(word):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count
ans = count_vowels('apple')
print(ans)

def count_consonants(word):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    count = 0
    for letter in word:
        if letter in consonants:
            count += 1
    return count
ans = count_consonants('apple')
print(ans)


def count_letters(word):
    return 'count_consonants' + 'count_vowels'
ans = count_letters('apple')
print(ans)

x = 48 % 24
print(x)