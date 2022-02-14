
class Dog():
    # Class object attributes, they are same for every class
    species = 'mammal'

    def __init__(self, breed, name, spots):

        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed = 'Huskie', name = 'Volkan', spots = True)
print(type(my_dog))
print(my_dog)
print(my_dog.species)
print()


class Dog():
    species = 'mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    # function in a class(object) is called method
    def bark(self, number):
        print(f'WOOF! My name is {self.name} and I am {number} years old')

my_dog = Dog('King Charles', 'Badem')
my_dog.bark(12)
print()


class Circle():
    # Class object attributes
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*self.pi  #self.pi = Circle.pi

    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.area)
print(my_circle.get_circumference())