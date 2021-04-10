#해싱

import sys

N, M = map(int, input().split())
dic1 = {} #이름 딕셔너리, 번호 딕셔너리 두 개 사용하면 해결. Key값을 이용해 해싱.
dic2 = {}

for i in range(N):
    poke = sys.stdin.readline().rstrip()
    dic1[poke] = str(i+1)
    dic2[str(i+1)] = poke
for j in range(M):
    poke = sys.stdin.readline().rstrip()
    if poke in dic1:
        print(dic1[poke])
    else:
        print(dic2[poke])
