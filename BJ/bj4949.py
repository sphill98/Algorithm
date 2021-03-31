class Stack: #기초적인 스택 클래스 구현
  def __init__(self):
    self.stk = []
  
  def size(self):
    return (len(self.stk))
  
  def empty(self):
    if len(self.stk) == 0:
      return 1
    else:
      return 0

  def top(self):
    if self.empty():
      return -1
    return (self.stk[-1])

  def pop(self):
    if self.empty():
      return -1
    else:
      return (self.stk.pop(-1))
  
  def push(self, x):
    self.stk.append(x)

bal = Stack()
ss = 0
while ss != '.':
  ss = input()
  if ss == '.':
    break
  for i in ss:
    if i == '(' or i == '[':
      bal.push(i)
    elif i == ')':
      if bal.top() == '(':
        bal.pop()
      else:
        bal.push(i)
    elif i == ']':
      if bal.top() == '[':
        bal.pop()
      else:
        bal.push(i)
  if bal.empty():
    print('yes')
  else:
    print('no')
  while not bal.empty():
    bal.pop()
