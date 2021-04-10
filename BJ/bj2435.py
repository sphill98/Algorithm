N, K = map(int, input().split())
s_lst = input().split()
lst = []
for t in s_lst:
  lst.append(int(t))
max_ = 0
for i in range(N-K+1):
  s = 0
  for j in range(K):
    s = s + lst[i+j]
  if i == 0:
    max_ = s
  else:
    if max_ < s:
      max_ = s
print(max_)
