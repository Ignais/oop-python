'''
Abstract classes and interfaces
'''

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    
    @abstractmethod
    def get_area(self):
        pass
    
    @abstractmethod
    def get_perimeter(self):
        pass

# You must provide suitable implementations for all its abstract methods
class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius
        
    def get_area(self):
        return pi * self.radius ** 2
    
    def get_perimeter(self):
        return 2 * pi * self.radius
    
if __name__ == "__main__":
    
    circle = Circle(50)
    
    print(f"The circle area is: {circle.get_area()}")
    print(f"The circle perimeter is: {circle.get_perimeter()}")