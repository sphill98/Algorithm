#BJ2606
#S3

#import sys

N = int(input())
M = int(input())

#Making Graph
G = ['GRAPH']
for i in range(N):
  G.append([])

for i in range(M): #edge list 작성
  e1, e2 = map(int, input().split())
  G[e1].append(e2)
  G[e2].append(e1)

dfs_visited = [1]

def DFS(G, u):
  for v in G[u]:
    if v not in dfs_visited:
      dfs_visited.append(v)
      DFS(G, v)

DFS(G, 1)

print (len(dfs_visited) - 1)
