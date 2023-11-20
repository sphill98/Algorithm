from collections import deque

#Variables
N, M, v = map(int, input().split())

G = [[] for i in range(N+1)]

dfs_lst = []
bfs_lst = []


dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)

for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in G:
    i.sort()

def DFS(v):
    dfs_visited[v] = True
    dfs_lst.append(v)
    for i in G[v]:
        if not dfs_visited[i]:
            DFS(i)

def BFS(v):
    queue = deque()
    bfs_visited[v] = True
    queue.append(v)
    bfs_lst.append(v)
    while queue:
        w = queue.popleft()
        for i in G[w]:
            if not bfs_visited[i]:
                queue.append(i)
                bfs_lst.append(i)
                bfs_visited[i] = True

DFS(v)
BFS(v)

for i in dfs_lst:
    print(i, end = ' ')
print('')
for i in bfs_lst:
    print(i, end = ' ')
