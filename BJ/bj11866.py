import sys

N, K = map(int, sys.stdin.readline().split())
lst = [x for x in range(1, N+1)]
ysp = []
i = 0
for r in range(N):
  i = (i + (K - 1)) % len(lst)
  o = lst[i]
  ysp.append(o)
  lst.remove(o)
print('<', end = '')

for i in range(len(ysp)):
  if i != len(ysp)-1:
    print(ysp[i],', ', sep = '', end = '')
  else:
    print(ysp[i], end = '')
print('>')
