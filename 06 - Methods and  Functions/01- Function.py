def hi():
    print('hello')
hi()

print()

def print_name(name='oben'): # fonksiyon içine isim girilmezse oben(default value) yazılacak
    print(name)
print_name()
print_name('cabbar')

print()

def add_num(num1, num2):
    return num1+num2
total = add_num(10, 20)
print(total)

print()

def print_sum(num3, num4):
    print(num3+num4)
total2 = print_sum(10, 20) # return yerine sadece print olduğu için total2 değerine kayıtlı olmadı
print(total2)

print()

def even_check(number):
    return number % 2 == 0
print(even_check(23))

print()

def even_print(list=[1, 2]): # def even_print(list): de olabilirdi default değersiz
    even_numbers = []
    for num in list:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass
    return even_numbers
print(even_print(list=[7, 98, 90]))

print()

def best_employee(hours_list):
    hours_max = 0
    employee_of_month = ''
    for employee, hours in hours_list:
        if hours > hours_max:
            hours_max = hours
            employee_of_month = employee
        else:
            pass
    return (employee_of_month, hours_max)

work_hours = [('Abby',100),('Billy',400),('Cassie',300)]
person, time = best_employee(work_hours)
print(person)

print()

from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0', '1', '2', '3']:
        guess = input('Pick a number: 0,1,2 or 3 ') # input always returns string
    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print('Correct')
        print(mylist)
    else:
        print('Wrong')
        print(mylist)

# INITIAL LIST
mylist = ['', 'O', '', '']
# SHUFFLE LIST
mixedup_list = shuffle_list(mylist)
# USER GUESS
guess = player_guess()
# CHECK GUESS
check_guess(mixedup_list, guess)