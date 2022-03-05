def hello(name='Jose'):
    print('The hello() function has been executed')
    
    def greet():
        print('\t This is inside the greet() function')
        # return '\t This is inside the greet() function'
    
    def welcome():
        return "\t This is inside the welcome() function"
    
    greet()
    # print(greet())    
    print(welcome())
    print("Now we are back inside the hello() function")

hello()



print()



def cool():

    def super_cool():
        print('I am very cool')

    return super_cool

some_func = cool() # cool function is assigned to some_func
some_func()



print()



# Function as Arguments
def hello():
    return 'Hi Jose!'

def other(func):
    print('Other code would go here')
    print(func())

other(hello)



print()



def new_decorator(func):

    def wrap_func():
        print("Code would be here, before executing the func")

        func()

        print("Code here will execute after the func()")

    return wrap_func

def func_needs_decorator():
    print("This function is in need of a Decorator")

new_func = new_decorator(func_needs_decorator)
new_func()


print()


@new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()


print()


# @new_decorator
def func_needs_decorator():
    print("This function is in need of a Decorator")

func_needs_decorator()