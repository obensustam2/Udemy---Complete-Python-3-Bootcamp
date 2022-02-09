##### SCOPE #####

# GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():

    # ENCLOSING
    name = 'Sammy'

    def hello():

        # LOCAL
        name = 'I AM LOCAL'

        print('Hello ' + name)

    hello()

greet()

print()

val = 50

def func(val):
    print(f'X is {val}')

    # LOCAL REASSIGNMENT
    val = 200
    print(f'I JUST LOCALLY CHANGED X TO {val}')

func(val)
print(val)