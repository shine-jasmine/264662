tests = int(input().strip())
while tests > 0:
  n = int(input().strip())
  arr = map(int, input().strip().split(' '))
  Lmin = arr[:]
  Rmin = arr[:]
  for i in range(1,n):
    Lmin[i] = min(Lmin[i-1], arr[i])
  for i in range(n-2, -1, -1):
    Rmin[i] = min(Rmin[i+1], arr[i])
  result = 'Yes'
  for i in range(1,n-1):
    if Lmin[i] < arr[i] and Rmin[i] < arr[i]:
      result = 'No'
      break
  print(result)
  tests -= 1