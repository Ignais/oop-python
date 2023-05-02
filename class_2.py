'''
In a Python class, you can define three different types of methods:

 1. Instance methods, which take the current instance, self, as their first argument
 2. Class methods, which take the current class, cls, as their first argument
 3. Static methods, which take neither the class nor the instance
'''
class Car:
    
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200
        
    def start(self):
        print("Starting the car...")
        self.started = True
        
    def stop(self):
        print("Stopping the car...")
        self.started = False
        
    def accelerate(self, value):
        if not self.started:
            print("Car is not started!")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f"Accelerating to {self.speed} km/h...")
        
    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f"Braking to {self.speed} km/h...")
        
    #special methods, dunder or magic methods
    
    def __str__(self):
        return f"{self.make}, {self.model}, {self.color}: ({self.year})"
    
    def __rep__(self):
        return (
            f"{type(self).__name__}"
            f'(make="{self.make}", '
            f'model="{self.model}", '
            f"year={self.year}, "
            f'color="{self.color}")'
        )


if __name__ == "__main__":
    
    ford_mustang = Car("Ford", "Mustang", 2022, "Black")
    
    Car.accelerate(ford_mustang, 100)
    
    Car.brake(ford_mustang, 100)
    
    Car.stop(ford_mustang)
    
    print(ford_mustang)
    
    #Car.start()