"""This module is created to practice conditional statements in python
created by Chandan on 10-07-2024"""

#Biggest of three numbers
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: "))
c = int(input("enter 3rd number: "))

if a>b and a>c:
    print(a," is biggest number")
elif b>a and b>c:
    print(b, " is biggest number")
else:
    print(c," is biggest number")