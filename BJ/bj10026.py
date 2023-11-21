from collections import deque

#Variables

G = []

N = int(input())

visited = [([False]*N) for _ in range(N)]

for i in range(N):
    G.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

norm_cnt = 0
weak_cnt = 0

def BFS(G, v, c):
    queue = deque()
    visited[v[0]][v[1]] = True # 0은 방문 1은 미방문
    queue.append(v)
    while queue: #queue가 빌 때까지 진행
        w = queue.popleft() #가장 첫번째 꺼내서
        for i in range(4):
            x = w[0] + dx[i] #위 아래 연결된 원소 찾기.
            y = w[1] + dy[i]
            if (x >= 0 and x < N) and (y >= 0 and y < N): #인덱스 에러 방지
                if G[x][y] == c and not visited[x][y]:
                    visited[x][y] = True
                    queue.append([x, y])


for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            v = [i, j]
            BFS(G, v, G[i][j])
            norm_cnt += 1

for i in range(N):
    for j in range(N):
        if G[i][j] == 'G':
            G[i][j] = 'R'

visited = [([False] * N) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            v = [i, j]
            BFS(G, v, G[i][j])
            weak_cnt += 1

print(norm_cnt, weak_cnt)
