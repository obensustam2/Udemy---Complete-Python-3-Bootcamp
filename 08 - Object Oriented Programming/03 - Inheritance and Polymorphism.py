#### INHERITANCE ####
class Animal():

    def __init__(self):
        print('Animal is created')

    def who_am_i(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

my_animal = Animal()
my_animal.eat()
my_animal.who_am_i()
print()


class Cat(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Cat is created')

    def who_am_i(self): # method is overwrited
        print('I am a cat')

    def meow(self):
        print('Meoww')

my_cat = Cat()
my_cat.who_am_i()
my_cat.eat()
my_cat.meow()
print()


#### POLYMORPHISM ####
class Dog():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says woof!'


class Snake():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' says Tshhhhh'

niko = Dog('niko')
felix = Snake('felix')

for pet in [niko,felix]:
    print(type(pet))
    print(pet.speak())
   




