"""This module is created to practice logical_operatos in python
created by Chandan on 08/07/2024"""

a,b,c = 21,20,19

print("a>b and a>c",a>b and a>c) #and means both should True #Result --> True
print("a>b and a<c",a>b and a<c) #Result --> False

a,b = True,False

print("a and b",a and b) #Result --> False
print("a or b",a or b) #Result --> True


#Note:
#any values other than ZERO --> this will be True, "0" as False
c,d = 10,0

print("c and d", c and d) #Result --> 0
print("c or d", c or d) #Result --> 10

#AND, if both are True, result will be right side value
#OR, if both are True, result will be left side value

c,d = 4,5
print("c and d", c and d) #both True, so right side value #Result --> 5
print("c or d", c or d) #both True, so left side value #Result --> 4

k,l,m,n = 40,30,20,10
print("k and l and m and n",k and l and m and n) #all are true, right will be the result --> 10
print("k or l or m or n",k or l or m or n) #all are true, left will be the result --> 40

k,l,m,n = 0,40,10,0
print("k and l and m and n",k and l and m and n) #true & false --> false, Result --> 0
print("k or l or m or n",k or l or m or n) #true or false --> true, Result --> 40 (left side value)