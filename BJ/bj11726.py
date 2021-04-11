def tile(n): #곰곰히 생각해보면 피보나치랑 다를 게 없음.
  if n == 1:
    return 1
  elif n == 2:
    return 2
  else:
    d = [0]*n
    d[0], d[1] = 1, 2
    for i in range(2, n):
      d[i] = d[i-1] + d[i-2]
    return d[n-1]

n = int(input())
print((tile(n)) % 10007)
