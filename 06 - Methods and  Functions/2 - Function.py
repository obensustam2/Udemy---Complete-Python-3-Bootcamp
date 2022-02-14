def myfunc(*finger): # parametre limitini(arbitrary number of arguments) ortadan kaldırdı
    return sum(finger)
print(myfunc(34,45,34,5,54)) # tuples tipinde data tutuyor

print()

def myfunc3(**kwargs): #dictionary tipinde data tutuyor
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit choice is {}'.format(kwargs['fruit']))
    else:
        print('I do not want to eat that')
myfunc3(fruit='apple', veggie='lettuce')

print()

def myfunc4(**k):
    print(k)
myfunc4(yemek='pilav')

print()

def myfunc2(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
myfunc2(10,20,30, fruit='orange', food='eggs')

print()

def myfunc5(*args):
    array = []
    for num in args:
        if num%2 == 0:
            array.append(num)
    return array
print(myfunc5(23,40,43,67,80))