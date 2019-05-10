# Here we are gonna learn about basics of python
# Basics of python
# variables in python
# syntax of python
# Functions
# commandline
# comments
# Numbers
# Strings
# Input




print("Hello world, This is TechByteCoder!")

# Variables

x = 10;
y = 20;
z = x + y
print(z)

# syntax
a = 10;
b = "Automation";
print ("Hello Sam " + b)


if 10>5:
    print("10 is greater than 5")



# Functions
def sum(a,b):
    print(a+b)

x = sum(20,30);


# Numbers
q = 5;#int
r = 2.5; #Float
s = 4j #compexnumber
print (type(q))
print (type(r))
print (type(s))



#Casting
x = int(3);
y = int(2.5);
z = float(1);
p = str(10);

print(x)
print(y)
print(z)
print(p)



#Strings

x = "Hello World"
print(x[1])    #here [1] is index which refers to the character 'H'!
print(len(x))   #To find the length of the string
print (x.upper()) #To convert into upper or Lower
print (x.strip()) #To strip the string to the correct format eg: "    Hello World" it will print "Hello WOrld"


print("Enter your Name: ")
x =input();
print("Hello, "+x)
print("How old are you? "+x)
y = input();
print("Wow, that's great "+x)



# Copy this Directory path and you can run this code on your cmd(Terminal)as well.