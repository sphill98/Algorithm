import sys
N = int(input())
lst = []

for i in range(N):
  start, end = map(int, sys.stdin.readline().split())
  lst.append([start, end])

lst.sort(key = lambda x : (x[1], x[0])) #가장 빨리 끝나는 순서대로 정렬한다. 다만, 가장 빨리 끝나는 것 중에서는 빨리 시작하는 것을 우선순위에 놓는다.
lst1 = []
conf = lst[0] #가장 빨리 시작하는 것부터 시작.
lst1.append(conf)
for i in range(1, N):
  if conf[1] <= lst[i][0]: #현재 회의가 끝나는 시각보다 다음 회의 시작 시간이 늦거나 같다면 해당 회의를 진행한다. 이미 정렬은 된 상태이기 때문에 현재 상태에선 최선의 선택이다.
    conf = lst[i]
    lst1.append(conf)
print(len(lst1))
