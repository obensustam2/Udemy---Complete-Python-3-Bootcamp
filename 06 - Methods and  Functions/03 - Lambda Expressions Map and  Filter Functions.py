###### MAP FUNCTION ######
def square(num):
  return num**2
my_nums = [1,2,3,4,5]
for item in map(square,my_nums): # apply the given function to given iterables(list)
  print(item)
print(list(map(square,my_nums)))

print()

def splicer(mystring):
  if len(mystring) % 2 == 0:
    return 'EVEN'
  else:
    return mystring[0]
names = ['bob', 'emre', 'orhan']
result = list(map(splicer,names))
print(result)

print()

###### FILTER FUNCTION ######
def check_even(num):
  return num % 2 == 0
mynums = [1, 2, 3, 4, 5, 67, 8]
result = list(filter(check_even, mynums))
print(result)

print()

###### LAMBDA FUNCTION ######
square = lambda a: a**2
print(square(3))

print()

a = list(map(lambda num: num**2, mynums))
print(a)

print()

x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

print()

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))

print()

full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name('guido', 'van rossum'))

print()

high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x: x * x))
print(high_ord_func(2, lambda x: x + 3))

print()

oddEven = lambda x: x % 2 and 'odd' or 'even'
print(oddEven(3))
