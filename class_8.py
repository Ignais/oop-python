'''
Extending an inherited method in a subclass, which
means that you’ll reuse the functionality
provided by the superclass and add new functionality on top
'''

class Aircraft:
    
    def __init__(self, thrust, lift, max_speed):
        self.thrust = thrust
        self.lift = lift
        self.max_speed = max_speed
        
    def show_technical_specs(self):
        print(f"Thrust: {self.thrust} kW")
        print(f"Lift: {self.lift} kg")
        print(f"Max speed: {self.max_speed} km/h")
        
class Helicopter(Aircraft):
    
    def __init__(self, thrust, lift, max_speed, num_rotors):
        super().__init__(thrust, lift, max_speed)
        self.num_rotors = num_rotors
    
    def show_technical_specs(self):
        super().show_technical_specs()
        print(f"Number of rotors: {self.num_rotors}")
        
if __name__ == "__main__":
    
    sikorsky_UH60 = Helicopter(1490, 9979, 278, 2)
    sikorsky_UH60.show_technical_specs()