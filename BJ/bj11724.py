#BJ11724
#S2

#import sys

N, M = map(int, input().split())

def DFS(G, u):
  for v in G[u]:
    if v not in dfs_visited:
      dfs_visited.append(v)
      DFS(G, v)

#Making Graph
G = ['GRAPH']
V = []
for i in range(N):
  G.append([])
  V.append(i+1)

for i in range(M): #edge list 작성
  e1, e2 = map(int, input().split())
  G[e1].append(e2)
  G[e2].append(e1)

conn_lst = []
while len(V) != 0:
  v0 = V[0]
  dfs_visited = [v0]
  DFS(G, v0)
  conn_lst.append(dfs_visited)
  tmp = set(V) - set(dfs_visited)
  V = list(tmp)

print (len(conn_lst))
