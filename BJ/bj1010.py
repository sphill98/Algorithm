n = int(input())

def comb(m, n):
  return (int(fact(m)/(fact(n)*fact(m-n))))

def fact(k):
  n = 1
  for i in range(k):
    n = n*(i+1)
  return n

for i in range(n):
    a, b = map(int, input().split())
    print (comb(b, a))
