import sys

N, K = map(int, input().split())
lst = []
for i in range(N):
  c = int(sys.stdin.readline())
  lst.append(c)
lst.sort(reverse = True) #금액이 큰 순서대로 정렬.
count = 0
for p in lst:
  if K // p != 0: #큰 금액의 동전부터 차례대로 사용해 원하는 금액을 맞추면 최소의 동전을 사용할 수 있다.
    count += (K // p)
    K -= ((K // p) * p)

print(count)
