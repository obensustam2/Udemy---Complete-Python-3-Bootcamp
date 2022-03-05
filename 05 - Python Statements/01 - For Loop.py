my_iterable = [1, 2, 3]
for item_name in my_iterable:
    print(item_name)

print()

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in list1:
    print(num)

print()

for num1 in list1:
    if num1 % 2 == 0:
        print(num1)

print()

for num2 in list1:
    if num2 % 2 == 0:
        print(num2)
    else:
        print('Odd number')

print()

list_sum = 0
for num3 in list1:
    list_sum = list_sum + num3
print(list_sum)

print()

list_sum2 = 0
for num4 in list1:
    list_sum2 += num4
print(list_sum)

print()

for letter in 'This is a string.':
    print(letter)

print()

tup = (1,2,3,4,5)

for t in tup:
    print(t)

print()

list2 = [(2,4),(6,8),(10,12)]
for tup in list2:
    print(tup)

print()

for (t1,t2) in list2:
    print(t1)

print()

d = {'k1':1,'k2':2,'k3':3}
for item in d:
    print(item)
print(list(d.items()))
print(list(d.keys()))
print(sorted(d.values()))

print()

for k,v in d.items():
    print(k)
    print(v)