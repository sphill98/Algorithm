import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())

G = [[] for _ in range(V + 1)]

INF = 10000000

d_lst = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((w, v))

d_lst[start] = 0

q = []
heapq.heappush(q, (0, start))

while q:
    c_weight, c_node = heapq.heappop(q)
    if d_lst[c_node] < c_weight:
        continue
    for n_weight, n_node in G[c_node]:
        n_dist = c_weight + n_weight
        if d_lst[n_node] > n_dist:
            d_lst[n_node] = n_dist
            heapq.heappush(q, (n_dist, n_node))

for i in range(1, V + 1):
    if d_lst[i] == INF:
        print('INF')
    else:
        print(d_lst[i])
