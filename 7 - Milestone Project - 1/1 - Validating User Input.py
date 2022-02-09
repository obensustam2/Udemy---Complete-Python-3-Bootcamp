# num = int(input('Enter a number '))
# print(float(num)+4)
#
# print()
#
# def user_choice():
#     choice = input('Please enter a value: ')
#     return int(choice)
#
# print(user_choice())
#
# print()
#
# mystring = '5n'
# print(mystring.isdigit()) # girilen string rakam mı diye kontrol ediyor. Digit=basamak, letter=harf
#
# print()

# def user_choice():
#     choice = 'wrong'
#     while choice.isdigit() == False:
#         print(choice.isdigit() == False)
#         choice = input('Please enter a number between 0 and 10 ')
#     return int(choice)
#
# print(user_choice())
#
# print()

# result = 3
# acceptable_values = [0,1,3,2,4]
# print(result in acceptable_values)


def user_choice():

    #INITIAL
    choice = 'wrong'
    acceptable_range = range(0,10)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input('Please enter a number between 0 and 10 ')

        # DIGIT CHECK
        if choice.isdigit() == False:
            print('Sorry that is not a digit')

        # RANGE CHECK
        else:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('Sorry you are out of range (0-10)')
                within_range = False

    return int(choice)

print(user_choice())


