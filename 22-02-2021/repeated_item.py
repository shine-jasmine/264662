# Write a program to find the repeated items in tuple
t=(10,5,20,10,20,20,95,50,60,80,80,95,95,95)
s=set()
for x in t:
    if t.count(x)>1:
        s.add(x)
print("Repeated Element Are:")
for x in s:
    print(x)
