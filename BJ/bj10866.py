import sys

class Deque: #기초적인 deque 클래스
  def __init__(self):
    self.dq = []
  
  def pushf(self, x): #덱 앞에 요소 추가
    self.dq.insert(0,x)

  def pushb(self, x): #덱 맨 뒤에 요소 추가
    self.dq.append(x)
  
  def popf(self): #덱 앞의 요소 제거
    if self.empty():
      return -1
    return (self.dq.pop(0))
  
  def popb(self): # 덱 맨 뒤의 요소 제거
    if self.empty():
      return -1
    return (self.dq.pop())
  
  def size(self): #덱의 사이즈 출력
    return (len(self.dq))
  
  def empty(self): #덱이 비어있는지 확인
    if self.size() == 0:
      return 1
    else:
      return 0
  
  def front(self): #덱의 맨 앞 요소 출력
    if self.empty():
      return -1
    return (self.dq[0])

  def back(self): #덱의 맨 뒤 요소 
    if self.empty():
      return -1
    return (self.dq[-1])

N = int(sys.stdin.readline())
dq = Deque()
for i in range(N):
  com = sys.stdin.readline().split()
  if com[0] == 'push_front':
    dq.pushf(com[1])
  elif com[0] == 'push_back':
    dq.pushb(com[1])
  elif com[0] == 'pop_front':
    print(dq.popf())
  elif com[0] == 'pop_back':
    print(dq.popb())
  elif com[0] == 'size':
    print(dq.size())
  elif com[0] == 'empty':
    print(dq.empty())
  elif com[0] == 'front':
    print(dq.front())
  elif com[0] == 'back':
    print(dq.back())
