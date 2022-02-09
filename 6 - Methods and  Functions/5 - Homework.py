def up_low(s):
    lowercase = 0
    uppercase = 0
    for char in s:
        if char.isupper():
            uppercase = uppercase + 1
        elif char.islower():
            lowercase = lowercase + 1
        else:
            pass
    print(f'Upper char number {uppercase}, Lower char number {lowercase}')

up_low('How U Doing Mate')

print()

def unique_list(lst):
    # Also possible to use list(set())
    x = []
    for a in lst:
        if a not in x:
            x.append(a)
    return x

print(unique_list([1,2,2,3,3,4,5,5,5]))

print()

def unique_list2(lst):
    list2 = list(set(lst)) # set unique elemanları buluyor
    return list2

print(unique_list2([1,2,2,3,3,4,5,5,5,9,9,9]))

print()

def multiply(numbers):
    total = 1
    for x in numbers:
        total = total * x
    return total

print(multiply([4,5,3]))

print()

def palindrome(s):
    s = s.replace(' ', '')  # This replaces all spaces ' ' with no space ''
    return s, s[::-1], s == s[::-1] # vice versa and check

print(palindrome('nurses went to hospital'))
print(palindrome('nurses run'))

print()

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet(unique harfler bulundu)
    alphaset = set(alphabet)
    print(alphaset)

    # Remove spaces from str1
    str1 = str1.replace(" ", '')
    print(str1)
    # Lowercase all strings in the passed in string
    # Recall we assume no punctuation
    str1 = str1.lower()
    print(str1)
    # Grab all unique letters in the string as a set
    str1 = set(str1)
    print(str1)
    # Now check that the alphabet set is same as string set
    return str1 == alphaset

print(ispangram("The quick brown fox jumps over the lazy dog"))
