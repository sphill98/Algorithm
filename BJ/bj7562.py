from collections import deque
import sys

def knightMove(size, start, end):
    dx = [-2, -2, -1, -1, 1, 1, 2, 2] #나이트가 이동할 수 있는 범위
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    visited = [([False] * size) for _ in range(size)] #방문기록 초기화
    x, y = start[0], start[1] #시작점
    xx, yy = end[0], end[1] #끝점
    visited[x][y] = True #시작점 방문 처리.
    q = deque()
    q.append((x, y, 0)) 
    while not visited[xx][yy]:
        c_x, c_y, c_l = q.popleft()
        for i in range(8):
            n_x = c_x + dx[i] #이동시켜준다.
            n_y = c_y + dy[i]
            n_l = c_l + 1
            if ((0 <= n_x) and (n_x < size)) and ((0<= n_y) and (n_y < size)):
                if not visited[n_x][n_y]:
                    if n_x == xx and n_y == yy: #찾으면
                        return n_l #현재 이동횟수 리턴.
                    visited[n_x][n_y] = True
                    q.append((n_x, n_y, n_l)) #못 찾으면 계속 진행.
    return 0 #이 경우는 base case. Start = End인 경우.

input = sys.stdin.readline

T = int(input()) #TestCase

for _ in range(T):
    L = int(input())  # BoardSize
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    print(knightMove(L, start, end))
