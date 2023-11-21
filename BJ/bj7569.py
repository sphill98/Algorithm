from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def BFS(G, vl):
    max_ = 0
    queue = deque()
    for v in vl:
        queue.append(v)
    while queue: #queue가 빌 때까지 진행
        w = queue.popleft() #가장 첫번째 꺼내서
        for i in range(6):
            x = w[0] + dx[i] #위 아래 연결된 원소 찾기.
            y = w[1] + dy[i]
            z = w[2] + dz[i]
            if (x >= 0 and x < H) and (y >= 0 and y < N) and (z >= 0 and z < M): #인덱스 에러 방지
                if G[x][y][z] == 0: #안 익은 토마토 만나면
                    G[x][y][z] = 1 #익힌 토마토로 바꿔줌.
                    queue.append([x, y, z, w[3] + 1])
                    max_ = max(max_, w[3]+1)
    return G, max_

M, N, H = map(int, input().split())

tmt_lst = []
start_lst = []

for i in range(H):
    tmt_lst.append([])
    for j in range(N):
        tmt_lst[i].append(list(map(int, input().split())))

for i in range(H):
    for j in range(N): #시작점 찾기
        for k in range(M):
            if tmt_lst[i][j][k] == 1:
                start_lst.append([i, j, k, 0])

tmt_lst, ans = BFS(tmt_lst, start_lst)

for i in range(H): #0 있으면 실패
    for j in range(N):
        for k in range(M):
            if tmt_lst[i][j][k] == 0:
                ans = -1

print(ans)
