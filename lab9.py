'''Zadanie1'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
point1 = Point()
point2 = Point(3, 4)

#print(f'Point1: ({point1.x}, {point1.y})')
#print(f'Point2: ({point2.x}, {point2.y})')

'''Zadanie2'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'
point1 = Point()
point2 = Point(3, 4)

#print(point1)
#print(point2)

'''Zadanie3'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

point1 = Point(3, 4)
point2 = point1 * 2
point3 = 2 * point1

#print(point1)
#print(point2)
#print(point3)

'''Zadanie4'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

point1 = Point(3, 4)
point2 = Point(3, 4)
point3 = Point(5, 6)
point4 = "Nie jest Point"

# print(point1 == point2)
# print(point1 == point3)
# print(point1 == point4)

'''Zadanie5'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

class Polygon:
    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        if isinstance(point, Point):
            self.points.append(point)
        else:
            raise TypeError("Oczekiwano instancji Point")

polygon = Polygon()
point1 = Point(1, 2)
point2 = Point(3, 4)

polygon.add_point(point1)
polygon.add_point(point2)

# for point in polygon.points:
#     print(point)

'''Zadanie6'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
class Polygon:
    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    def __str__(self):
        points_str = ', '.join(str(point) for point in self.points)
        return f'Polygon[{points_str}]'

polygon = Polygon()
polygon.add_point(Point(2, 3))
polygon.add_point(Point(1, 1))
polygon.add_point(Point(0, 0))

# print(polygon)

'''Zadanie7'''
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
class Polygon:
    def __init__(self):
        self.points = []

    def add_point(self, point: Point):
        self.points.append(point)

    def __str__(self):
        points_str = ', '.join(str(point) for point in self.points)
        return f'Polygon[{points_str}]'

    def __getitem__(self, item):
        try:
            return self.points[item]
        except TypeError:
            raise TypeError("Indeks musi być liczbą całkowitą lub wycinkiem")

polygon = Polygon()
polygon.add_point(Point(2, 3))
polygon.add_point(Point(1, 1))
polygon.add_point(Point(0, 0))

print(polygon)

print(polygon[0])
print(polygon[1:3])

try:
    print(polygon['a'])
except TypeError as e:
    print(e)
