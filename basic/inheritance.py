'''
Program to demonstrate inheritance in python

Builds on the 'Vehicle' class in 'classes_and_objects.py'
'''

class Vehicle:
    def __init__(self, name, color, engine, company_name, win_number):
        self.name = name
        self.num_wheels = 4
        self.color = color
        self.engine = engine
        self.company_name = company_name
        self.win_number = win_number
    
    def drive(self):
        print(f"Vehicle {self.name} moving forward")
    
    def start(self):
        print(f"Vehicle {self.name} turned on")
        
    def stop(self):
        print(f"Vehicle {self.name} stopping now")
    
    def print_attr(self): #TODO see if some inbuilt method can be used
        print(f"Name = {self.name}")
        print(f"Num wheels = {self.num_wheels}")
        print(f"Color = {self.color}")
        print(f"Engine = {self.engine}")
        print(f"Company name = {self.engine}")
        print(f"WIN number = {self.win_number}")
    
    def print_num_wheels(self):
        print(f"{self.name} ::  Num wheels = {self.num_wheels}")
        
class Car(Vehicle):
    def __init__(self, name, color, engine, company_name, win_number):
        super().__init__(name, color, engine, company_name, win_number)
        self.num_wheels = 4
            
class Truck(Vehicle):
    def __init__(self, name, color, engine, company_name, win_number):
        super().__init__(name, color, engine, company_name, win_number)
        self.num_wheels = 8
    
if __name__ == "__main__":
    c = Car('Baleno', 'Blue', 'Suzuki', 'Nexa', 123456789)
    c.print_num_wheels()
    
    t = Truck('Hammer', 'Black', 'Toyota', 'Bajaj', 987654321)
    t.print_num_wheels()
 