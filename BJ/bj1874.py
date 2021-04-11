#pypy3

import sys

n = int(input())
lst = [x for x in range(1, n+1)]
a_n = []

for i in range(n):
  a_n.append(int(sys.stdin.readline()))

stk = [1] #어차피 1은 무조건 push해야함.
stk_s = '+'
i, j = 1, 0 

while True:
  if len(lst) == 0: #리스트가 비었다면 pop이 모두 진행됐으므로, 스택수열이 된다는 뜻이다.
    for s in stk_s:
      print(s)
    break
  if len(stk) == 0 or stk[-1] != a_n[j]:
    if i == len(lst): #범위를 초과해서 추가하려고 한다면 스택수열이 되지 않는다.
      print('NO')
      break
    stk.append(lst[i])
    stk_s += '+'
    i += 1 
  else:
    a = stk.pop() #스택에서 하나씩 뺄 때마다 리스트에서도 같이 빼줄 것.
    stk_s += '-'
    j += 1
    i -= 1 #스택에는 작은 수부터 들어가기 때문에, 큰 수가 빠지면 인덱스가 줄어야 먼저 들어온 수를 가르킬 수 있다.
    lst.remove(a)
