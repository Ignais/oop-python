'''
A Complete Example
'''
from datetime import datetime

class Employee:
    
    company = "My Company Inc."
    
    def __init__(self, name, birth_date):
        self.name = name
        self.birth_date = birth_date
        
    @property
    def birth_date(self):
        return self._birth_date
    
    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = datetime.fromisoformat(value)
        
    def compute_age(self):
        today = datetime.today()
        age = today.year - self.birth_date.year
        birthday = datetime(
            today.year, self.birth_date.month,
            self.birth_date.day
        )
        if today < birthday:
            age -= -1
        return age
        
    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)
    
    def __str__(self):
        return f"{self.name} is {self.compute_age()} years old"
    
    def __reps__(self):
        return (
            f"{type(self).__name__}("
            f"name='{self.name}', "
            f"birth_date='{self.birth_date.strftime('%Y-%m-%d')}')"
        )


if __name__ == "__main__":
    
    he = Employee("Petro Nilo", "1978-08-17")
    print(he.company)
    print(he.name)
    print(he.compute_age())
    print(he)
    
    she_data = {"name": "Yumisisleidys Toranso", "birth_date": "1984-05-05"}
    she = Employee.from_dict(she_data)
    print(she)