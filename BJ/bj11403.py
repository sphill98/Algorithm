INF = 1e9

N = int(input())

G = []

for _ in range(N):
    G.append(list(map(int, input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            G[i][j] = max(G[i][j], (G[i][k] * G[k][j]))

for i in range(N):
    for j in range(N):
        print(G[i][j], end = ' ')
    print()
