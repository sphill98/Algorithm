from collections import deque
N = int(input())
dq = deque([x for x in range(1, N+1)]) #list 쓰면 런타임 에러 나길래 덱 씀. 
while len(dq) > 1:
  dq.popleft()
  dq.append(dq.popleft())

print(dq[0])
