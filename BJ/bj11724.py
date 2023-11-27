#BJ11724
#S2

import sys
from collections import deque

def BFS(u):
    q = deque()
    q.append(u)
    visited[u] = True
    while q:
        v = q.popleft()
        for e in G[v]:
            if not visited[e]:
                visited[e] = True
                q.append(e)

input = sys.stdin.readline

N, M = map(int, input().split())

G = [[] for _ in range(N+1)]

for i in range(M): #Graph 작성
    e1, e2 = map(int, input().split())
    G[e1].append(e2)
    G[e2].append(e1)

visited = [False] * (N + 1)

cnt = 0

for i in range(1, N + 1):
    if not visited[i]:
        BFS(i) #한 번 할 때마다 연결리스트 발견
        cnt += 1
        
print(cnt)
