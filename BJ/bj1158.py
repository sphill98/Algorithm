N, K = map(int, input().split())

lst = [i for i in range(1, N+1)]
y_lst = []

st = K-1
print('<', end = '')
while len(lst) != 0:
    a = lst[st]
    print(a, end = '')
    lst.remove(a)
    if len(lst) != 0:
        print(', ', end = '')
        st = (st + K - 1) % len(lst)
print('>', end = '')
