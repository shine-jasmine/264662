# Write a program to change the nth value to (n+1)th in list
l=[1,2,3,4,5,6,7,8,9,10]
temp=l[0]
for i in range(len(l)-1):
    l[i]=l[i+1]
l[len(l)-1]=temp
print(l)
