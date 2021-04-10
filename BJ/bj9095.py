import sys

def summ(n): #피보나치 다이나믹이랑 똑같은데 식만 다름.
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 4
  else:
    d = [0]*n
    d[0], d[1], d[2] = 1, 2, 4
    for i in range(3, n):
      d[i] = d[i-1] + d[i-2] + d[i-3]
    return d[n-1]

T = int(input())

for i in range(T):
  k = int(sys.stdin.readline())
  print(summ(k))
