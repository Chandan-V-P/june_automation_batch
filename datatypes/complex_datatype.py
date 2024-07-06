'''This file is Created to practice complex data type in Python
created by chandan on 06/25/2024'''

a = 1.5+1j #Here 1.5 is Real Value & 1 is imaginary Value
print("Value of a is", a)
print("type of a is", type(a))
print("id of a is", id(a))

b = 1.5+1j
print("Value of b is", b)
print("type of b is", type(b))
print("id of b is", id(b))

c = 1.5-1j
print("Value of c is", c)
print("type of c is", type(c))
print("id of c is", id(c))

d = -1j #complex data type should contain atleast imaginary value
print("Value of d is", d)
print("type of d is", type(d))
print("id of d is", id(d))

print("Methods available in boolean", dir(a))
print("real value of a", a.real) #Result --> 1.5
print("imaginary value of a", a.imag) #Result --> 1
