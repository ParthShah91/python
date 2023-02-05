'''
Program to demonstrate list and its methods
'''
import random

l = random.sample(range(0, 100), 10)

print(f"l = {l}")

l.append(123)
l.append(145)
print(f"l (after append) = {l}")

l.sort()
print(f"Sorted list (in ascending order) = {l}")

l.sort(reverse=True)
print(f"Sorted list (in descending order) = {l}")

l.reverse()
print(f"List (after reverse) = {l}")

l.pop()
print(f"List (after single pop method) = {l}")
l.pop()
print(f"List (after single pop method) = {l}")