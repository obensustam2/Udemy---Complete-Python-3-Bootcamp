try :
    # WANT TO ATTEMPT THIS CODE
    # MAY HAVE AN ERROR
    result = 10 + 10
    #result = 10 + '10'
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print(result)
    print("good job")

print()

try:
    f = open('testfile', 'r')
    f.write("write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("Hey you have an OS error")
finally:
    print("I always run")

print()

def ask_for_int():
    try:
        result = int(input("Please provide number: "))
    except:
        print("Whoops! That is not a number")
    finally:
        print("End of try/except/finally")
ask_for_int()

print()

def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")

ask_for_int()
