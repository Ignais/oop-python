'''
Exploring Specialized Classes From the Standard Library.
Data classes
'''
from dataclasses import dataclass

@dataclass
class ThreeDpoint:
    
    x: int or float
    y: int or float
    z: int or float
    
    @classmethod
    def from_sequence(cls, sequence):
        return cls(*sequence)
    
    @staticmethod
    def show_intro_message(name):
        print(f"Hey {name}! This is your 3D Point")
        

if __name__ == "__main__":
    
    point_1 = ThreeDpoint(1.3, 9, 3.5)
    print(point_1)
    
    point_2 = ThreeDpoint(2, 3, 4)
    print(point_1 == point_2)
    
    pt = ThreeDpoint.from_sequence([4,2,7])
    print(pt)
