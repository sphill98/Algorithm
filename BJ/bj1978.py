import math

n = int(input())

lst = input().split()
count = 0

def isPrime(p): #에라토스테네스의 체
  k = 2
  if p < 2:
    return False
    
  while k <= math.sqrt(p):
    if p % k == 0:
      return False
    k += 1
  return True

for i in range(n):
  if isPrime(int(lst[i])):
    count += 1

print (count)
