import heapq
import sys

input = sys.stdin.readline

V = int(input())
E = int(input())

G = [[] for _ in range(V + 1)]

INF = 100000001 #최댓값으로 초기화

d_lst = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((w, v))

start, end = map(int, input().split())
d_lst[start] = 0

q = []
heapq.heappush(q, (0, start)) #(d, v) 출발점부터 v까지 거리를 d라고 저장.

while q:
    c_weight, c_node = heapq.heappop(q) #최솟값을 우선으로 뽑기 위해 heap 사용.
    if d_lst[c_node] < c_weight: #현재노드까지 거리가 기존 최단거리보다 멀면 무시.
        continue
    for n_weight, n_node in G[c_node]: #다음 노드를 체크한다.
        n_dist = c_weight + n_weight #새로운 거리 = 기존 거리에서 한 번 더 간 거리.
        if d_lst[n_node] > n_dist:
            d_lst[n_node] = n_dist #거리 업데이트
            heapq.heappush(q, (n_dist, n_node)) #업데이트 해준다.

print(d_lst[end])
