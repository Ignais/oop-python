'''
In Python, you can use multiple inheritance.
'''

class Vehicle:
    
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color
        
    def start(self):
        print("Starting the engine...")
        
    def stop(self):
        print("Stoping the engine...")
        
    def show_technical_specs(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Color: {self.color}")
        
class Car(vehicle):
    def drive(self):
        print("Dreiving on the road...")
        
class Aircraft(Vehicle):
    def fly(self):
        print("Flying in the sky"...):
            
class FlyingCar(Car, Aircraft):
    pass