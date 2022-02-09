class Sample():
    pass

my_sample = Sample()
print(type(my_sample))
print()


class Dog():
    def __init__(self, breed):
        self.my_attribute = breed

my_dog = Dog(breed = 'Labrador')
print(type(my_dog))
print(my_dog.my_attribute)
print()


class Dog():
    def __init__(self, breed, name, spots=True):
        # Attributes
        # Arguments are taken and assigned by using self
        self.breed = breed
        self.name = name
        self.spots = spots

my_dog = Dog(breed='Labrador', name='Keke', spots=False)
print(type(my_dog))
print(my_dog)
print(my_dog.spots)
print()
