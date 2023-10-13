N, M, K = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

f_max = lst[N - 1]
s_max = lst[N - 2]

ans = 0

while M != 0:
    for i in range(K):
        ans += f_max
        M -= 1
        if M == 0:
            break
    if M != 0:
        ans += s_max
        M -= 1
    
    
print(ans)
