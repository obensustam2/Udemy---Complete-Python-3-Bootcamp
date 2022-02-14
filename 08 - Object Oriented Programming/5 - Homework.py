class Cylinder:

    pi = 3.14

    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        return self.pi * self.radius**2 * self.height

    def surface_area(self):
        return 2 * self.pi * self.radius * ( self.radius + self.height)

my_cylinder = Cylinder(2,3)
print(f'Volume is {my_cylinder.volume()}')
print(f'Surface area is {my_cylinder.surface_area()}')
print()


class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        return ((self.coor1[0] - self.coor2[0])**2 + (self.coor1[1] - self.coor2[1])**2)**0.5
        #x1, y1 = self.coor1
        #x2, y2 = self.coor2
        #return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


    def slope(self):
        return (self.coor2[1] - self.coor1[1])/(self.coor2[0] - self.coor1[0])
        #x1, y1 = self.coor1
        #x2, y2 = self.coor2
        #return (y2 - y1) / (x2 - x1)

coordinate1 = (3,2)
coordinate2 = (8,10)
my_line = Line(coordinate1, coordinate2)
print(f'Distance is {my_line.distance()}')
print(f'Slope is {my_line.slope()}')