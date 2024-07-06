"""This module is created to practice frozenset data type in python
created by Chandan on 03/07/2024"""

s = {1,1,1,2,3,4,5,5}
s = frozenset(s)

print("values in s:", s)
print("type of s:", type(s))
print("memory of s:", id(s))

print("methods available for frozenset:", dir(s))
