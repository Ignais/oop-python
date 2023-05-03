'''
Using Inheritance and Building Class Hierarchies
'''

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._started = false
        
    def start(self):
        print("Starting engine...")
        self._started = True
        
    def stop(self):
        print("Stoping engine...")
        self._started = False
        
class Car(Vehicle):
    def __init__(self, make, model, year, num_seats):
        #In Car, you use super() to call the .__init__() method on Vehicle
        super().__init__(make, model, year)
        self.num_seats = num_seats
        
    def drive(self):
        print(f"Driving my {self.make} - {self.model} on the road")
    
    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_seats} seats'

class Motocycle(Vehicle):
    
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)
        self.num_wheels = num_wheels
        
    def ride(self):
        print(f'Riding my "{self.make} - {self.model}" on the road')

    def __str__(self):
        return f'"{self.make} - {self.model}" has {self.num_wheels} wheels'
    
'''
Note: You can create class diagrams to represent class hierarchies that are based
on inheritance. However, that’s not the only relationship that can appear between
your classes.

With class diagrams, you can also represent other types
of relationships, including:

    Composition, which expresses a strong has-a relationship.
        For example, a robot has an arm. If the robot stops existing,
        then the arm stops existing too.
    Aggregation, which expresses a softer has-a relationship.
        For example, a university has an instructor.
        If the university stops existing, the instructor doesn’t stop existing.
    Association, which expresses a uses-a relationship.
        For example, a student may be associated with a course.
        They will use the course. This relationship is common in
        database systems where you have one-to-one, one-to-many,
        and many-to-many associations.

'''