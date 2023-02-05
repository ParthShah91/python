'''
Program to print fibonacci sequence
'''

def fibonacci(num):
    #print("num = ", num)
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
        
if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(4))
    print(fibonacci(5))
    
    