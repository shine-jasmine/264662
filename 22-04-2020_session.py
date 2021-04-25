"Hello Python"
print(__doc__) #Doc is used to access the docstring
"""Any string that is not assigned would be considered as comment"""

a=input("Enter the first Number:")
b=input("Enter the second number :")
res=a+b
print(res)
print(type(res))
res=int(res)
print(type(res))

hh,mm,yyyy=10,12,2021
print(hh,mm,yyyy)

x=10
y=2.3
s1="hello"
ch='A'
flag=True
c1=2+3j
print(type(c1))
print(isinstance(x,int)) #Returns True if the variable is of specific type


fval=2.3
ival=int(fval) #2
print(ival)

ch='A'
#ival=int(ch,10)
aval=ord(ch) #65
print(aval) #ord is used to give the ascii value of character

s1="2378"
ival=int(s1)
print(ival) #2348
s2="45a64"
# ival=int(s2) #It will generate an error as int with base 10 otherwise we can use int(s2,16) here 16 is the base
# print(ival)

ival=23
s3=str(ival)
print(s3)

hval="23"
ival=int(hval,16)
print("49",ival)

s4="12.235"
fval=float(s4)
print("53",fval)
print(int(0x1D))
print(hex(45))
print(oct(0o23))
print(bin(13))
print(int(0b11011))

#id is used to know the memory location
a=5
print(id(a))
a="Diptiman"
print(id(a))


a=32
b=10
c=a/b
d=a//b
print(c,d)
x=2
y=5
z=x**y
q=x*(y-5)
x+=5
print(q,x)

a=10
b=2
c=0
# and, & in python-> and returns true if both the operand are true(in this case it returns the highest value) whereas
# & return the bitwise operations between the two values.
print("and and or")
print(a and b)
print(b and a)
print(a and c)
print(c and b)
print(a or b)
print(b or a)
print(a or c)
print(c or b)

s1="Hello"
s2="Hello"
ch='e'
c2='x'
print(s1==s2)
print(s1 is s2)
print(ch in s1)
print(c2 not in s2)

xval = -12.785
print(abs(xval)) #gives the absolute value
print(round(xval,2)) #gives the rounded value

# For Concatinating string we can use + operator
s1="abcd"
s2='xyz'
print(s1+s2)

# Converting string to integer and adding
s1="10"
s2="20"
s3=int(s1)+int(s2)
print(s3)

# String Operations
s1="abcd"
s1*=3
print(s1)
s1+="xyz"
print(s1)
print("hello " * 3) #hello hello hello
print(4 * "hello ") #hello hello hello hello

# Swapping of Number
a,b=10,20
a,b=b,a
print(a,b) #20 10

# Swapping can be done using XOR operations
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)  # 20 10

n=2378
a=(n/100)%10
print(a) # 3.780000000000001
b=(n/10)%10
print(b) # 7.800000000000011
c=(n%100)/10
print(c) # 7.8
d=(n%1000)/100
print(d) # 3.78
