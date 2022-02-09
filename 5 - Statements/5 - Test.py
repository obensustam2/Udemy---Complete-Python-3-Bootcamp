for num in range(0,100):
    if num == 0:
        print(num)
    elif num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

print()

st = 'Create a list of the first letters of every word in this string'
mylist = [word[0] for word in st.split()]
print(mylist)

