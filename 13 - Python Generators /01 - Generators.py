# Non memory efficient
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(10))


print()


# Generator function for the cube of numbers (power of 3), Memory efficient
def gencubes(n):
    for num in range(n):
        yield num**3

for x in gencubes(10):
    print(x)


print()


# Memory efficient
def genfibon(n):
    """
    Generate a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for num in genfibon(10):
    print(num)


print()


# Non memory efficient
def fibon(n):
    a = 1
    b = 1
    output = []
    
    for i in range(n):
        output.append(a)
        a,b = b,a+b
        
    return output

print(fibon(10))