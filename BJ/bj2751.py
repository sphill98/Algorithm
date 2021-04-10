import sys

def Merge(lx, rx):
  li, ri = 0, 0
  mx = []
  while li < len(lx) and ri < len(rx):
    if lx[li] <= rx[ri]:
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

lst = []
for i in range(N):
  lst.append(int(sys.stdin.readline()))

lst = MergeSort(lst)
for i in lst:
    print (i)
