def func():
    try:
        for i in ['a','b','c']:
            print(i**2)
    except TypeError:
        print("Exception TypeError")
func()

print()

def func2():
    try:
        x = 5
        y = 0
        print(z = x/y)
    except ZeroDivisionError:
        print("Exception ZeroDivisionError")
    finally:
        print("All Done")
func2()

print()

def ask():
    while True:
        try:
            a = int(input("Enter a integer number: "))
            a_sqr = a**2
        except:
            print("It is not an integer")
            continue
        else:
            print(a_sqr)
            break
ask()
