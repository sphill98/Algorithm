from collections import deque
import sys

input = sys.stdin.readline

def BFS(start, mx, my):
    dx = [0, 0, -1, 1] #다음 노드로 이동하기 위한 방향 설정.
    dy = [-1, 1, 0, 0] 
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        G[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if ((0 <= nx) and (nx < mx)) and ((0 <= ny) and (ny < my)):
                if G[nx][ny] == 1: #배추가 있다 = 방문하지 않음.
                    G[nx][ny] = 0 #방문처리
                    q.append((nx, ny))

T = int(input()) #TestCase

for _ in range(T):
    M, N, K = map(int, input().split())
    G = [([0] * M) for i in range(N)] #그래프 초기화
    ans = 0
  
    for i in range(K):
        y, x = map(int, input().split())
        G[x][y] = 1
      
    for i in range(N):
        for j in range(M):
            if G[i][j] == 1: #첫 배추 찾고
                BFS((i, j), N, M)
                ans += 1 #한 집단 추가
    print(ans)




