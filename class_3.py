'''
Example of a minimal ThreeDPoint class
that implements the iterable protocol
'''
class ThreeDPoint:
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __iter__(self):
        yield from (self.x, self.y, self.z)
    
    #class methods to custom Python classes
    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)
    
    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")
    
    def __repr__(self):
        return f"{type(self).__name__}({self.x}, {self.y}, {self.z})"
    
    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point!")
        
        
if __name__ == "__main__":
    
    _list = list(ThreeDPoint(4, 8, 16))
    
    _point = ThreeDPoint.from_sequence((4, 8, 16))
    
    print(_list)
    
    print(_point)
        
    print(_point.from_sequence((3, 6, 8)))
    
    print(ThreeDPoint.show_intro_message("Pythonista"))
    