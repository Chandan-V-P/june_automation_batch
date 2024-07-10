'''can be performed on sequence,
i.e, string, list, tuple, dict, set, frozenset'''

#IN
a = 'ETL Automation'
print("'ETL' in \"a\" is",'ETL' in a) #Result --> True
print("'E' in \"a\" is",'E' in a) #Result --> True
print("'n' in \"a\" is",'n' in a) #Result --> True

b = [1,2,3,4]
#IN & NOT IN
print("'ETL' not in \"a\" is",'ETL' not in a) #Result --> False
print("1 not in \"b\" is",1 not in b) #Result --> False

c = [1,2,3,4,5]
d = [1,2,3]
print("1,2 not in c is:",2,3 not in c) #Result --> False
print("c in d is:", c in d) #list inside list #complete list 'c' is not present in 'd', hence False
print("1,2,3 in d", 1,2,3 in d) #Result --> True

c = [1,2,3,4,5]
d = [1,2,3,[4,5]]
print("[4,5] in d is:",[4,5] in d) #Result --> True


#dict --> we should search with keys only
d1 = {1:'ETL', 2:'Automation', 3:'Testing'}
print("1 in d1", 1 in d1) #True

#if we want to search the values, we should use d.values()
print("'ETL' in d1", 'ETL' in d1.values()) #Result --> True

print("1 in d1", 1 in d1.keys()) #Result --> True


d1 = {1:'ETL', 2:'Automation', 3:'Testing'}
d2 = {1:'ETL', 2:'Automation', 3:'Testing'}

#this is mutable, hence the memory allocation will be diff
print("d1 is d2", d1 is d2) #Result --> False
print("d1 == d2", d1==d2) #Result --> True


