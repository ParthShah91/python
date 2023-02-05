'''
Program to generate factorial of a given number. The program demonstrates use of recursion in python. It generates a random list of 5 numbers in the range 1 to 10 and calculates factorial using the 'factorial' method
'''
import random

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1) 

if __name__ == "__main__":
    test_list = random.sample(range(0, 10), 5)
    print(f"test_list = {test_list}")
    for num in test_list:
        print(f"Factorial of {num} is ", factorial(num))