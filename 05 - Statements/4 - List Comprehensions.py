myString = 'hello'
mylist = []
for letter in myString:
    mylist.append(letter)
print(mylist)

print()

myString = 'hello'
mylist = []
mylist = [letter for letter in myString]
print(mylist)

print()

myString2 = 'hi'
mylist2 = []
mylist2 = [x for x in myString2]
print(mylist2)

print()

mylist = [x for x in range(0, 11)]
print(mylist)

print()

mylist = [x**2 for x in range(0, 11)]
print(mylist)

print()

mylist = [x for x in range(0, 11) if x % 2 == 0]
print(mylist)

print()

mylist = [x**2 for x in range(0, 11) if x % 2 == 0]
print(mylist)

print()

celsius = [0, 10, 20.1, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

print()

fahrenheit = []
for temp in celsius:
    fahrenheit.append((9/5)*temp + 32)
print(fahrenheit)

print()

mylist = []
for x in [2, 4, 6]:  # nested loops
    for y in [1, 10, 100]:
        mylist.append(x*y)
print(mylist)

print()

mylist = [x*y for x in [2, 4,  6] for y in [1, 10, 100]]
print(mylist)