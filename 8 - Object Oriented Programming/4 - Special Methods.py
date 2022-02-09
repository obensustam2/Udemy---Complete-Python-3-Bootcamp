#
# mylist = [1,2,3]
# print(len(mylist))
#
# class Sample():
#     pass
#
# mysample = Sample()
# len(mysample)

class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self): # str
        return f'{self.title} by {self.author}'

    def __len__(self): # len
        return self.pages

    def __del__(self): # del
        print('A book object has been deleted')

my_book = Book('Python rocks', 'Jose', 200)
print(my_book) # it prints the string version of the object
print(str(my_book))
print(len(my_book))
del my_book # delete variable/object
print(my_book)
