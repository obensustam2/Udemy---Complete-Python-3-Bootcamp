x = 0
while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1

print()

x = 0
while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1
else:
    print('All Done!')

print()

x = 0
while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x = x + 1
    if x == 3:
        print('x=3')
    else:
        print('continuing...')
        continue

print()


x = 0
while x < 10:
    print('x is currently: ', x)
    print(' x is still less than 10, adding 1 to x')
    x += 1
    if x == 3:
        print('Breaking because x=3')
        break
    else:
        print('continuing...')
        continue

print()


x = 0
while x < 10:
    print('x is currently: ', x)
    x += 1
    if x == 9:
        print('Breaking because x=9')
        break
    elif x == 5:
        print('x=5')
        continue
        print("This text can't be displayed because it is after continue, code jumps to the first line of while loop")

