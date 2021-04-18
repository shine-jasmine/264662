n = int(input())

for x in range(1, n,2):
    if x % 3 == 0 and x % 5 == 0:
        print("fizzbuzz")
        continue
    elif x % 3 == 0:
        print("fizz")
        continue
    elif x % 5 == 0:
        print("buzz")
        continue
    else:
        print(x)