"""This module is created to practice Arithmetic operators in python
created by Chandan on 05/07/2024"""

#PEMDAS Rule or BODMAS Rule

a = (8+2)*3/2 #1st Paranthesis --> 10*3/2 --> Mul & Div have same priority (Which ever comes first)
#10*3/2 --> 30/2 --> 15.0
print("(8+2)*3/2 is:",a)

b = (8+2)/3**2+3*2
#10/3**2+3*2 --> 10/9+3*2 --> 10/9+6 --> 1.11+6 --> 7.11
print("b = (8+2)/3**2+3*2 is:",b)

c = (20+10)*(15/5)
# 30 * (15/5) --> 30*3.0 --> 90.0
print("(20+10)*(15/5) is:",c)