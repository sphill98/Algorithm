#BJ2581
#S5

import math

def isPrime(p): #에라토스테네스의 체
  k = 2
  if p < 2:
    return False
    
  while k <= math.sqrt(p):
    if p % k == 0:
      return False
    k += 1
  return True

lst = []

M = int(input())
N = int(input())

for i in range(M, N+1):
  if isPrime(i):
    lst.append(i)

if len(lst) == 0:
  print(-1)
else:
  print(sum(lst))
  print(lst[0])
