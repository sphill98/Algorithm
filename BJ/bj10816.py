N = int(input())
lst1 = input().split()
dic = {}
for s in lst1:
  if s in dic:
    dic[s] += 1
  else:
    dic[s] = 1
M = int(input())
lst2 = input().split()

for i in lst2:
  if i in dic:
    print (dic[i], end = ' ')
  else:
    print (0, end = ' ')
