# Write a program to check if the input number is
# -real number
# -float number
# -string
# -complex number
# -Zero(0)

x=input("Enter the number :")
if x==0:
    print("Zero")
elif isinstance(x,complex):
    print("Complex Number")
# elif isinstance(float(x),float):
#     print("Float Number")
# elif isinstance(int(x),int):
#     print("Real Number")
# elif isinstance(x,str):
#     print("String")
