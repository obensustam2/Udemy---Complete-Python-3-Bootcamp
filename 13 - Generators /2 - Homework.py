# Yield Examples

def gensquares(N):
    for n in range(N):
        yield n**2

for x in gensquares(10):
    print(x)


print()


import random

def rand_num(low,high,n):
    for a in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)


print()


