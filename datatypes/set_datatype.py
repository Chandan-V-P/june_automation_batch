"""This module is created to practice set data types in python
and created by Chandan on 03/07/2024"""

s1 = {1,2,3,4,5}
s2 = {3,4,5}

#Intersection
print("s1 Intersection s2:", s1.intersection(s2)) #{3, 4, 5}

#Difference
print("s1 Difference s2:", s1.difference(s2)) #{1, 2}

#ADD Method in SET (there is no Append, Extend in SET)
s1.add(6)
print("s1 Value:", s1) #{1, 2, 3, 4, 5, 6}


#POP Method (Don't use, don't know which value set will delete)
print("s1 Value before pop:", s1)
s1.pop()
print("s1 Value After pop1:", s1) #Result --> {2, 3, 4, 5, 6}
s1.pop()
print("s1 Value After pop2:", s1) #Result --> {3, 4, 5, 6}

#CLEAR Method --> This will remove all the elements
print("s1 Before Clear:", s1) #Result --> {3, 4, 5, 6}
s1.clear()
print("s1 After Clear:", s1) #Result --> set()
