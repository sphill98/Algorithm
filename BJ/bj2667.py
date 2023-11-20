from collections import deque

#Variables

Gr = []

N = int(input())

for i in range(N):
    Gr.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

lst = []

def BFS(G, v):
    cnt = 0
    queue = deque()
    G[v[0]][v[1]] = '0' # 0은 방문 1은 미방문
    queue.append(v)
    while queue: #queue가 빌 때까지 진행
        w = queue.popleft() #가장 첫번째 꺼내서
        cnt += 1
        for i in range(4):
            x = w[0] + dx[i] #위 아래 연결된 원소 찾기.
            y = w[1] + dy[i]
            if (x >= 0 and x < N) and (y >= 0 and y < N): #인덱스 에러 방지
                if G[x][y] == '1':
                    queue.append([x, y])
                    G[x][y] = '0'
    return G, cnt


for i in range(N):
    for j in range(N):
        if Gr[i][j] == '1':
            v = [i, j]
            Gr, tmp = BFS(Gr, v)
            lst.append(tmp)

lst.sort()
print(len(lst))
for s in lst:
    print(s)
