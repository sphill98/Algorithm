N = int(input())

def isVPS(s):
  if s[0] == ')' or s[-1] == '(': #시작이 )거나 끝이 (면 False
    return False
  else:
    count = 0
    for i in s:
      if count == 0 and i == ')': 
        return False
      if i == '(': #(면 하나씩 증가.
        count += 1
      else: #)면 하나씩 감소.
        count -= 1
    if count == 0: #전부 사라지면 균형잡힘.
      return True
    else:
      return False

for i in range(N):
  s = input()
  if isVPS(s):
    print('YES')
  else:
    print('NO')
