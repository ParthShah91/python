'''
Program to demonstrate simple use of map filter reduce
'''

from functools import reduce

def calc_square(n):
    return n*n
    
def number_in_range(n):
    if n > 20 and n < 50:
        return n

def sumOfNums(n1, n2):
    return n1 + n2
    
if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9,10]

    print(f"l = {l}")

    squares = list(map(calc_square, l)) #Executes 'calc_square' method on all members in list 'l'
    print(f"squares = {squares}")
    
    l1 = list(filter(number_in_range, squares)) # Executes 'number_in_range' method on all members in list 'squares'
    print(f"Numbers in between 20 and 50 are : {l1}")
    
    l2 = list(reduce(sumOfNums, l))
    print(f"Sum of members of list {l} is : {l2}")
    
    