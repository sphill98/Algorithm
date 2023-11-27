from collections import deque

def a2b(start, end):
    q = deque()
    q.append((start, 1))
    while q:
        p, lev = q.popleft()
        if p == end:
            return lev
        if p <= end:
            for s in [2 * p, 10 * p + 1]:
                if s <= end: #찾는값보다 큰 값은 넣을 필요 없음. 이미 실패.
                    q.append((s, lev + 1)) #찾는값에 레벨 하나 추가해줌.

    return -1


A, B = map(int, input().split())

print(a2b(A,B))
