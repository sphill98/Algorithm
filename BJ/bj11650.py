#11650
from operator import itemgetter

N = int(input())
tup = []
for i in range(N):
  x, y = map(int, input().split())
  tup.append((x, y))
tup.sort(key=itemgetter(0,1))
for i in range(N):
  print(tup[i][0], tup[i][1])
