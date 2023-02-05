'''
Program to demonstrate use of *args and **kwargs
*args - variable number of arguments
**kwargs - arguments with keyword eg: foo(reverse=True)
'''

def demoArgs(*args):
    print("\nArguments to func to demo args are :->")
    for arg in args:
        print(arg)

def demoKwargs(**kwargs):
    print("\nArguments to func to demo kwargs are :->")
    for key, item in kwargs.items():
        print(f"{key} = {item}")

def demoArgsKwargs(*args, **kwargs):
    print("\nArguments to func to demo args and kwargs are :->")
    
    print("Args are :")
    for arg in args:
        print(arg)
    
    print("Keyword args are :")
    for key, item in kwargs.items():
        print(f"{key} = {item}")
        
if __name__ == "__main__":
    demoArgs("sachin", "tendulkar", 100)
    demoKwargs(name="virat kohli", runs="12000", country="India")
    demoArgsKwargs(123, "one", "two", 45.67, name="dhoni", position="captain")