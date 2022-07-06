import sys
'''
import os
f = open('input.txt', 'r')

sys.stdin = f 
'''
def isIncident(x, y, M, N): #인접한 node를 찾는 알고리즘
    L = []
    if x + 1 < M:
        L.append((x+1, y))
    if y + 1 < N:
        L.append((x, y+1))
    if x - 1 >= 0:
        L.append((x-1, y))
    if y - 1 >= 0:
        L.append((x, y-1))
    return L
        
def BFS(G, start_lst, M, N): #BFS
    L = []
    L.append([])
    L[0] = start_lst #이미 익어있는 토마토들의 좌표를 0에 추가.
    i = 0
    while len(L[i]) != 0:
        if len(L) < i + 2:
            L.append([])
        for s in L[i]: #각각의 익어있는 토마토와 인접한 것들이 익는데 걸리는 시간을 잰다.
            K = isIncident(s[0], s[1], M, N)
            for t in K:
                xx, yy = t[0], t[1]
                if G[xx][yy] == 0:
                    G[xx][yy] = 1
                    L[i+1].append((xx, yy))
        i = i + 1
    return G, i-1

M, N= map(int, sys.stdin.readline().split())

box = []

for i in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))
    
reds = []

for y in range(M):
    for x in range(N):
        if box[x][y] == 1:
           reds.append((x, y)) #이미 익어있는 토마토의 좌표를 추가한다.
           
farm, day = BFS(box, reds, N, M)

flag = True
for y in range(M):
    for x in range(N):
        if farm[x][y] == 0:
            print(-1)
            flag = False
            break
    if not flag:
        break

if flag:
    print(day)
