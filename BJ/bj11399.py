N = int(input())
s_lst = input().split()
lst = []
for i in s_lst:
  lst.append(int(i))
lst.sort() #시간 적게 걸리는 사람부터 정렬하면 해결.
g_lst = []
for i in range(N):
  g_lst.append(sum(lst[:i+1])) #순서대로 시간 더해서 리스트에 추가함. 각 사람들의 걸리는 시간 리스트.


print(sum(g_lst))
