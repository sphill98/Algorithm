#BJ1389
#S1

#import sys

N, M = map(int, input().split())

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

def BFS(G, u):
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

def Bacon(lst): #베이컨 수를 구하는 과정
  bacon_n = 0
  for n in range(len(lst)):
    bacon_n += n*len(lst[n]) #n이 단계, lst[n]은 단계가 n인 vertex들의 집합이다.
  return bacon_n

dic = []

for u in V:
  bfs_visited = [[u]]
  BFS(G, u)
  dic.append([u, Bacon(bfs_visited)])

dic.sort(key = lambda x : (x[1], x[0])) #베이컨 수가 가장 작은 것부터 정렬. 값이 같으면 작은 vertex가 우선.

print(dic[0][0])
