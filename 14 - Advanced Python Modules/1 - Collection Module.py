from collections import Counter


myList = [1,1,1,1,2,2,2,2,2,2,3,3,3,3,3]
print(Counter(myList))


print()


myList = ['a', 'a', 0, 7, 7, 7]
print(Counter(myList))


print()


print(Counter('fafWAEFwaefdewaf'))


print()


s = 'How many times does each word show up in this sentence word times each each word'
words = s.lower().split()
print(words)
print(Counter(words))


print()


letters = 'aaabajdkafkjashfjkagfAasdffaf'
count = Counter(letters)
print(count.most_common(3))
print(list(count))


print()


from collections import defaultdict

d = {1: '10'}
print(d)
print(d[1])


print()


myTuple = (10, 20, 30)
print(myTuple[2])

print()


from collections import namedtuple 

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age=5, breed='Husky', name='Orbay')
print(sammy)
print(sammy.age)
print(sammy[2])
