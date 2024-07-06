"""This file is created to practice boolean data type
and created by Chandan on 06/25/2024"""

a = True
print("Value of a is", a)
print("type of a is", type(a))
print("id of a is", id(a))

b = True
print("Value of b is", b)
print("type of b is", type(b))
print("id of b is", id(b))

c = False
print("Value of c is", c)
print("type of c is", type(c))
print("id of c is", id(c))

d = False
print("Value of d is", d)
print("type of d is", type(d))
print("id of d is", id(d))

print("Methods available in boolean", dir(a))
print("__add__ adding a & b", a.__add__(b)) #True value is 1 & False Value is 0 in Python #Result --> 2
print("adding a & c", a.__add__(c)) #Result --> 1