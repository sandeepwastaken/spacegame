import math as m

class Person:
    def __init__(self, name, age, gender, race):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race

    def introduce(self):
        print(f"Hello, I am {self.name}, I am a {self.race} {self.gender} who is {self.age} years old.")

person1 = Person("Sandeep", 15, "Male", "Indian")
person1.introduce()

# ----------------------------------------
# Create a class for a rectangle, which has member, x and y (position) of the top left corner
# There are 2 more members which are height and width
# Member functions would be getting parameter and area

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    def distance(self, other):
        return(m.sqrt((self.x - other.x)**2 + (self.y - other.y)**2))


class Rect:
    def __init__(self, x, y, height, width):
        self.position = Point(x, y)
        self.height = height
        self.width = width
    
    def paramater(self):
        return(self.height*2 + self.width*2)
    
    def area(self):
        return(self.height*self.width)
    
    def center(self):
        return(Point(self.width/2 + self.position.x, self.height/2 + self.position.y))
    
    def distance(self, other):
        selfCenter = self.center()
        otherCenter = other.center()
        return selfCenter.distance(otherCenter)


rect1 = Rect(-10, -15, 15, 20)
rect2 = Rect(30, 10, 15, 20)
point1 = Point(0, 0)
point2 = Point (5, 9)
print(rect1.paramater())
print(rect1.area())
print(rect1.center())
print(point1.distance(point2))
print(rect1.distance(rect2))

# Calculate a function called "collide"
# Takes another rectangle and returns "true" if they are colliding (overlapping)
# and if not it returns "false"
