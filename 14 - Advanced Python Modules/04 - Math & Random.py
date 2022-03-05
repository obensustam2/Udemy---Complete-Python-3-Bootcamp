import math

value = 4.99
print(math.floor(value))
print(round(value))
print(math.log(math.e))
print(math.log(100, 10))

print()

import random

print(random.randint(0, 100))
random.seed(101)
print(random.randint(0, 100))
print(random.randint(0, 100))

print()

myList = list(range(0, 20))
print(myList)
x = random.choice(myList)
print(x)