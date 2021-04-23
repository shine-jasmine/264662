# Write a program to convert a list into a nested dictionary of keys
l=[10,20,30,40,50]
actual=current={}
for x in l:
    current[x]={}       #Creating a empty dict with key x
    current=current[x]  #Referencing the current to curremt key value
print(actual)
