a = 10
b = 20
c = 10
print("id of a is:",id(a))
print("id of b is:",id(b))
print("id of c is:",id(c))
print("a is b",a is b) #here 'is' is identity operator #a & b have diff memory location #Result --> False
print("a is c",a is c) #same memory location #Result --> True

print("a is not b",a is not b) #Result --> True
print("a is not c",a is not c) #Result --> False


#list #mutable have diff memory locations
a = [1,2,3]
b = [1,2,3]
print("a is b",a is b) #in list, even though same values, memory location will be diff, Hence False
#but individual index value memory will be same
print("a[0] is b[0]",a[0] is b[0]) #Result --> True


#tupe --> immutable --> same memory location
a = (1,2,3)
b = (1,2,3)
print("a is b",a is b) #immutable will be have same memory location #Result --> True
print("a[0] is b[0]",a[0] is b[0]) #Result --> True