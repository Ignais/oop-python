'''
Overriding an inherited method in a subclass,
which means that you’ll completely discard the
functionality from the superclass and provide new
functionality in the subclass
'''
cass Worker:
    
    def __init__(self, name, address, hourly_salary):
        
        self.name = name
        self.address = address
        self.hourly_salary = hourly_salary
        
    def show_profile(self):
        print("== Worker profile ==")
        print(f"Name: {self.name}")
        print(f"Address: {self.address}")
        print(f"Hourly salary: {self.hourly_salary}")
        
    def calculate_payroll(self, hours=40):
        return self.hourly_salary * hours
    
class Manager(Worker):
    
    def __init__(self, name, address, hourly_salary, hourly_bonus):
        
        super().__init__(name, address, hourly_salary)
        self.hourly_bonus = hourly_bonus
    
    # Manager has to override .calculate_payroll() completely.
    def calculate_payroll(self, hours=40):
        return (self.hourly_bonus + self.hourly_bonus) * hours