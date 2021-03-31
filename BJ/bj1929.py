import math

def isPrime(p): #에라토스테네스의 
  k = 2
  if p < 2:
    return False
    
  while k <= math.sqrt(p):
    if p % k == 0:
      return False
    k += 1
  return True

lst = []

M, N = map(int, input().split())

for i in range(M, N+1):
  if isPrime(i):
    print(i)
