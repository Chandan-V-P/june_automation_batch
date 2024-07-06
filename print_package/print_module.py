''' This file is created to practice print function
    created by: chandan on 06/21/2024
'''

#we can combine the strings using seperator, Here the separator is "-"
print("Hello Guys!","Welcome to ETL Automation Testing",sep="-") #Result --> Hello Guys!-Welcome to ETL Automation Testing
print("Hello Guys! Welcome to ETL Automation Testing") #Without Separator "-"

str1 = "Hello"
str2 = "Automation"
str3 = "World"
#strings seperate with separator
print(str1,str2,str3,sep="#") #Result --> Hello#Automation#World
print(str1,str2,str3,sep="|") #With Single pipe separator #Result --> Hello|Automation|World

source_count = 10
target_count = 20
print(source_count,target_count,source_count+target_count,sep=",") #Result --> 10,20,30

print("Sum of Source & Target Count is: ", source_count+target_count) #Result --> Sum of Source & Target Count is:  30

#format string
print(f"Source Count is {source_count}, Target Count is {target_count}, Difference is {source_count-target_count}")

print("Hello","Brother","Miss You",sep="-",end="\t")
print("Bye") #Result --> Hello-Brother-Miss You	Bye
