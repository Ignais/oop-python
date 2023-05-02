import math

'''
It’s important to note that the validation also runs at instantiation
time when you call the class constructor to create new instances of Circle.
This behavior is consistent with your validation strategy.
'''

class Circle:
    
    def __init__(self, radius):
        self.radius = radius
    
    #use the @property decorator to write the getter method.
    @property
    def radius(self):
        return self._radius
    
    #To define the setter method (@attr_name.setter) of a property-based attribute.
    @radius.setter
    def radius(self, value):
        if not (isinstance(value, int)  or isinstance(value, float)) or value <= 0:
            raise ValueError("positive number expected")
        self._radius = value
    
    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)

class Square:
    def __init__(self, side):
        self.side = side
    
    #use the @property decorator to write the getter method.
    @property
    def side(self):
        return self._side

    #To define the setter method (@attr_name.setter) of a property-based attribute.
    @side.setter
    def side(self, side):
        if not (isinstance(side, int) or isinstance(side, float)) or side <= 0:
            raise ValueError("positive number expected")
        self._side = side
        
    def calculate_area(self):
        return round(self._side ** 2, 2)
    
'''
This class is pretty similar to Circle, and the repetition starts looking odd.
Then you think of using a descriptor to abstract away the validation process.
'''
class PositiveNumber:
    
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, instance, owner):
        return instance.__dict__[self._name]
    
    def __set__(self, instance, value):
        if not (isinstance(value, int) or isinstance(value, float)) or value <= 0:
            raise ValueError("positive number expected")
        instance.__dict__[self._name] = value
        
class CircleTwo:
    
    radius = PositiveNumber()
    
    def __init__(self, radius):
        
        self.radius = radius
    
    def calculate_area(self):
        return round(math.pi * self.radius**2, 2)
    
class SquareTwo:
    
    side = PositiveNumber()
    
    def __init__(self, side):
        self.side = side
        
    def calculate_area(self):
        return round(self.side**2, 2)
    
'''
In a Python class, using the .__slots__ attribute can help you
reduce the memory footprint of the corresponding instances. 
'''
class Point:
    
    __slot__ = ("x", "y")
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
'''
Adding a .__slots__ to your classes allows you to provide a series of
allowed attributes. This means that you won’t be able to add new attributes
to your instances dynamically. If you try to do it, then you’ll get an
AttributeError exception.
'''

class SomeObject():
    counter = 0
    
    def __init__(self):
        
        type(self).counter += 1
        
if __name__ == "__main__":
    
    fig = Circle(3.45)
    figura = vars(fig)
    print(figura)
    print(f"{fig.radius} radius")
    fig.radius = 100
    print(f"{fig.radius} new radius")
    print(f"{fig.calculate_area()} meters cuadrades")
    
    obj = SomeObject()
    obj_2 = SomeObject()
    obj.counter = 100
    print(f"{SomeObject.counter} {obj.counter}")
    
    circle = Circle(45)
    circle_two = CircleTwo(45)
    
    print(f"First circle area: {circle.calculate_area()}")
    print(f"Second circle area: {circle_two.calculate_area()}")