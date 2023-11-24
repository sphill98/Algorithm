import sys

input = sys.stdin.readline

N, M = map(int, input().split())

G = [([0] * (N + 1)) for _ in range(N + 1)]

ans = [0] * (N + 1)
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            G[i][j] = max(G[i][j], (G[i][k] * G[k][j]))

for i in range(1, N + 1):
    for j in range(1, N + 1):
        ans[i] += G[i][j]
        ans[j] += G[i][j]

print(ans.count(N - 1))
