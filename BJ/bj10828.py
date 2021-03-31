import sys

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

N = int(sys.stdin.readline())

stk = Stack()

for i in range(N):
  mess = sys.stdin.readline().split()
  if mess[0] == 'push':
    stk.push(int(mess[1]))
  elif mess[0] == 'pop':
    print(stk.pop())
  elif mess[0] == 'size':
    print(stk.size())
  elif mess[0] == 'empty':
    print(stk.empty())
  else:
    print(stk.top())
