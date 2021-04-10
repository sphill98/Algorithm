import sys

N, M = map(int, input().split())

ls = set() #단순히 리스트를 사용하면 런타임에러 뜬다. Set을 이용해 빠르게 연산해준다.
lss = set()

for i in range(N):
  ls.add(sys.stdin.readline().rstrip()) #듣지도 못한.
for i in range(M):
  lss.add(sys.stdin.readline().rstrip()) #보지도 못한

lslst = list(ls.intersection(lss)) #교집합 = 
lslst.sort()
print(len(lslst))

for i in lslst:
  print(i)
