#BJ1260
#S2

#import sys

N, M, v0 = map(int, input().split())

#Making Graph
G = ['GRAPH']
for i in range(N):
  G.append([])

for i in range(M): #edge list 작성
  e1, e2 = map(int, input().split())
  G[e1].append(e2)
  G[e2].append(e1)

for i in range(N): #작은 순서대로 방문하게 하기 위해 sorting
  G[i+1].sort()

dfs_visited = [v0]
bfs_visited = [[v0]]

def DFS(G, u): #DFS
  for v in G[u]:
    if v not in dfs_visited:
      dfs_visited.append(v)
      DFS(G, v)

def BFS(G, u): #BFS
  b_visit = [u]
  b = 0
  while len(bfs_visited[b]) != 0:
    bfs_visited.append([])
    for v in bfs_visited[b]:
      for w in G[v]:
        if w not in b_visit:
          bfs_visited[b+1].append(w)
          b_visit.append(w)
    b += 1

DFS(G, v0)
BFS(G, v0)

for s in dfs_visited:
  print(s, end = ' ')
print('')
for s in bfs_visited:
  for k in s:
    print(k, end = ' ')
