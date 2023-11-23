N, K = map(int, input().split())

P = [([0] * (N + 1)) for _ in range(K + 1)] 

lst = []

for i in range(N): #2차원 배열
    w, v = map(int, input().split())
    lst.append((w, v))
lst.sort(key = lambda x:x[0]) #무게가 중요하니까 무게를 기준으로 정렬.

for i in range(K+1):
    for j in range(1, N+1): #무게가 가장 작은 것부터 따져본다.
        if lst[j - 1][0] > i: #무게가 가방 한계보다 크면 그 물건 빼고 최대값.
            P[i][j] = P[i][j - 1]
        else: #무게가 가방한계 안으로 들어오면..
            val = lst[j-1] 
            P[i][j] = max(P[i][j - 1], val[1] + P[i - val[0]][j-1]) #물건 넣는 거랑 안 넣는 거랑 비교.

print(P[-1][-1])

