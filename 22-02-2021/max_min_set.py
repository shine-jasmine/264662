# Write a program to find the maximum and minimum in set
s={50,0,-1,60,89,90,-100}
print("Maximum in set is ",max(s))
print("Minimum in set is ",min(s))

# It can be done using the algorithm
minv=100000000
maxv=-100000000
for x in s:
    if minv>x:
        minv=x
    if maxv<x:
        maxv=x
print("Maximum in set: ",maxv)
print("Minimum in set: ",minv)
