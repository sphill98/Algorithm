#매개변수 탐색을 활용한 문제

import sys

def check(lst, l, N):
  tmp = 0
  for i in lst:
    if i >= l:
      tmp = tmp + (i - l)
     
  if tmp >= M:
    return True
  else:
    return False


N, M = map(int, sys.stdin.readline().split())
lst = sys.stdin.readline().split()
n_lst = []
for i in lst :
  n_lst.append(int(i))
l0 = 0 #반드시 문제해결이 되는 지점을 시작점으로.
l2 = max(n_lst) #반드시 문제가 해결되지 않는 지점을 끝점으로

while l0 + 1 < l2:
  l1 = (l0 + l2) // 2 #이분 탐색처럼 중간값을 이용한다.
  if check(n_lst, l1, M):
    l0 = l1
  else:
    l2 = l1
    
print(l0)
