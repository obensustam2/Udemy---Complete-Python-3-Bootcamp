for num in range(10):
    print(num)

print()

for num in range(5,10):
    print(num)

print()

for num in range(4,16,3):
    print(num)

print()

index_count = 0
for letter in 'abcde':
    print("At index {} the letter is {}".format(index_count,letter))
    index_count += 1

print()

index_count = 0
for letter in 'abcde':
    print(f'At index {index_count} the letter is {letter}')
    index_count += 1

print()

for i,letter in enumerate('abcde'): # index count yapmaya gerek yok
    print("At index {} the letter is {}".format(i,letter))

print()

mylist1 = [1,2,3,4,5]
mylist2 = ['a','b','c','d','e']
mylist3 = [100, 200, 300]
for item in zip(mylist1, mylist2, mylist3):
    print(item)

print()

for a,b,c in zip(mylist1, mylist2, mylist3):
    print(c)

print()

state = 'x' in ['x', 'y', 'z']
print(state)

print()

state = 3 not in ['x', 'y', 'z']
print(state)

print()


mylist = [10,20,30,40, 100]
print(min(mylist))
print(max(mylist))

print()

from random import shuffle
mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist) # inplace function
print(mylist)

print()

from random import randint
print(randint(0,100))

print()

# result = input('Enter Something into this box: ')
# print(result)
# print()

number = 0

for number in range(10):
    if number == 5:
        break    # break here

    print('Number is ' + str(number))

print('Out of loop')

print()

number = 0

for number in range(10):
    if number == 5:
        continue    # continue here

    print('Number is ' + str(number))

print('Out of loop')

print()

number = 0

for number in range(10):
    if number == 5:
        pass    # pass here

    print('Number is ' + str(number))

print('Out of loop')














