'''
A mixin class provides methods that you can reuse in many
other classes. Mixin classes don’t define new types,
so they’re not intended to be instantiated. You use their
functionality to attach extra features to other classes quickly.
'''

import json
import pickle

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class SerializerMixin:
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    def to_pickle(self):
        return pickle.dumps(self.__dict__)
    
class Employee(SerializerMixin, Person):
    
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

if __name__ == "__main__":
    
    ignais = Employee("Ignais La Paz", 45,  50000)
    print(ignais.to_json())
    print(ignais.to_pickle())