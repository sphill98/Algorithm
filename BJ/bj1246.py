def counter(egg, price, cust):
  if egg < cust:
    return price*egg
  else:
    return price*cust
    

n, m = map(int, input().split())
lst = []
for i in range(m):
  p = int(input())
  lst.append(p)
lst.sort()

ans = [0, 0]

for k in range(m):
  tmp = counter(n, lst[k], m-k)
  if ans[1] < tmp:
    pr = lst[k]
    ans = [pr, tmp]

print(ans[0], ans[1])
