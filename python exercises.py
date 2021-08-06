print("Hello World!") #First Command

if 5 > 2:
    print("Five is greater than two!") #If Statements

"""
Multiline comment
"""

carname = 'Volvo'#Assign String Variable

"""
x = 50 #Assign Number Variable
y = 10
print (x + y) #Addition
"""

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

myfirst_name = 'John'

x = y = z = 'Orange'


def myfunc():
 global a
a = "fantastic"


b = 5
print (type(x)) #Prints out Data Type 'int'

c = 20.5
print(type(c)) #Prints out Data Type 'float'

print(type(fruits)) #Prints out Data Type 'list'

d = ("apple", "banana", "cherry")
print(type(d)) #Prints out Data Type 'tuple'

e = {"name": "John", "age": 36}
print(type(e)) #Prints out Data Type 'dict'

f = True
print(type(f)) #Prints out Data Type 'bool'

b = 5
b = float(b) #Convert to Float 

c = int(c) #Convert to int

g = 5
g = complex(g) 
print(g) #Convert to complex number

h = "Hello World"
print(len(h)) #Length of String Character

txt = "Hello World"
i = txt[0]
print(i) #Find first character of string variable

j = txt[2:5]
print(j)

txt_2 = " Hello World "
txt_2 = txt_2.strip() #Remove White space from beginning or end
txt_2 = txt_2.upper() #Make value Upper Case
txt_2 = txt_2.lower() #Make value Lower Case
txt_2 = txt_2.replace("H", "J")
print(txt_2)

age = 36
lne = "My name is John, and I am {}" #Correct Syntax - Placeholder 
print(lne.format(age))
