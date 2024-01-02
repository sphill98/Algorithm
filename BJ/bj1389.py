#BJ1389
#S1

#import sys
#input = sys.stdin.readline
N, M = map(int, input().split())

INF = 1e9
lst = [[]] * (N + 1)
fw_lst = [([INF]*(N+1)) for _ in range(N + 1)]

for i in range(1, N + 1):
    fw_lst[i][i] = 0

for i in range(M):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)
    fw_lst[a][b], fw_lst[b][a] = 1, 1

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            fw_lst[i][j] = min(fw_lst[i][j], fw_lst[i][k] + fw_lst[k][j])

sum_ = INF
ans = 0
for k in range(1, N + 1):
    i = N + 1 - k
    temp = sum(fw_lst[i])-fw_lst[i][0]
    if temp <= sum_:
        sum_ = temp
        ans = i

print(ans)
