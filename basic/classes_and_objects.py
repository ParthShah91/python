'''
Program to demonstrate usage of class and objects 
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
        

if __name__ == "__main__":
    v1 = Vehicle('Baleno', 'Celestial blue', 'Suzuki', 'Nexa', 123456789)
    v1.print_attr()
    v1.start()
    v1.drive()
    v1.drive()
    v1.stop()
    
    print("\n\n")
        
    v2 = Vehicle('Nexon', 'Tree Green', 'Tata', 'Tata', 987654321)
    v2.print_attr()
    v2.start()
    v2.stop()
    