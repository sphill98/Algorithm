import sys

def isBig(s, t):
  if len(s) > len(t):
    return True
  elif len(s) < len(t):
    return False
  else:
    return (s > t)


def Merge(lx, rx):
  li, ri = 0, 0
  mx = []
  while li < len(lx) and ri < len(rx):
    if isBig(rx[ri], lx[li]):
      mx.append(lx[li])
      li += 1
    else:
      mx.append(rx[ri])
      ri += 1
  if li == len(lx) and ri < len(rx):
    while ri < len(rx):
      mx.append(rx[ri])
      ri += 1
  elif ri == len(rx) and li < len(lx):
    while li < len(lx):
      mx.append(lx[li])
      li += 1
  return mx

def MergeSort(x):
  if len(x) == 1:
    return x
  else:
    lx = x[ : (len(x) // 2)]
    rx = x[(len(x) // 2) : ]
    return Merge(MergeSort(lx), MergeSort(rx))



N = int(sys.stdin.readline())
w_lst = []
for i in range(N):
  word = sys.stdin.readline().rstrip('\n')
  if word not in w_lst:
    w_lst.append(word)

lst = MergeSort(w_lst)

for i in lst:
  print(i)
