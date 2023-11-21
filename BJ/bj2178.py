from collections import deque

#Variables

G = []

N, M = map(int, input().split())

for i in range(N):
    G.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(G, v):
    cnt = 0
    queue = deque()
    G[v[0]][v[1]] = '0' # 0은 방문 1은 미방문
    queue.append(v)
    while queue: #queue가 빌 때까지 진행
        w = queue.popleft() #가장 첫번째 꺼내서
        if w[0] == N - 1 and w[1] == M - 1:
            return w[2] + 1
        for i in range(4):
            x = w[0] + dx[i] #위 아래 연결된 원소 찾기.
            y = w[1] + dy[i]
            if (x >= 0 and x < N) and (y >= 0 and y < M): #인덱스 에러 방지
                if G[x][y] == '1':
                    queue.append([x, y, w[2]+1])
                    G[x][y] = '0'


print(BFS(G, [0,0,0])) # x, y, 층 수
