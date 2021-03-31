#매개변수 탐색을 활용한 문제

import sys

def check(lst, l, N):
  tmp = 0
  for i in lst:
    tmp = tmp + (i // l)
  if tmp >= N:
    return True
  else:
    return False


K, N = map(int, sys.stdin.readline().split())
lst = []
for i in range(K):
  lst.append(int(sys.stdin.readline()))
l0 = 1 #반드시 문제해결이 되는 지점을 시작점으로.
l2 = (sum(lst) // N) + 1 #반드시 문제가 해결되지 않는 지점을 끝점으로

while l0 + 1 < l2:
  l1 = (l0 + l2) // 2 #이분 탐색처럼 중간값을 이용한다.
  if check(lst, l1, N):
    l0 = l1
  else:
    l2 = l1
    
print(l0)
