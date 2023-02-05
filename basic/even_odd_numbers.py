'''
The program is a demo program to find even odd numbers in a list and to demonstrate list comprehension
It will generate the input list of size 5 by choosing random values between 1 and 100
'''

import random

l = random.sample(range(1, 100), 5)
print("list = ", l)

e = [x for x in l if x % 2 == 0]

if e:
    print("List containing even numbers = ", e)
else:
    print("List is empty")
    
o = [x for x in l if x % 2 != 0]
if o:
    print("List containing odd numbers = ", o)
else:
    print("List is empty")