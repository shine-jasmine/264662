# Write a program to print the second smallest element in list
import sys

l=[20,3,2,2,5,8,9,9,10,20]
minv=min(l)
smin=sys.maxsize
for x in l:
    if x!=minv:
        if smin>x:
            smin=x
print("Second Smallest element in list :",smin)
