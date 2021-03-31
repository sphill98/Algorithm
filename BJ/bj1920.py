#이분탐색

N = int(input())
n_lst_s = input().split()
M = int(input())
m_lst_s = input().split()
n_lst = []
m_lst = []
def mergeSort(x): #MergeSort 알고리즘
    if len(x) > 1:
      mid = len(x) // 2
      lx, rx = x[:mid], x[mid:]
      mergeSort(lx)
      mergeSort(rx)

      li, ri, i = 0, 0, 0
      while (li < len(lx)) and (ri < len(rx)):
        if lx[li] <= rx[ri]:
          x[i] = lx[li]
          li += 1
        else:
          x[i] = rx[ri]
          ri += 1
        i += 1
      x[i:] = lx[li:] if li != len(lx) else rx[ri:]
    return x

def binSearch(n, x): #이분탐색 
  l, r = 0, len(x) - 1
  while l <= r:
    m = (l + r) // 2
    if n > x[m]:
      l = m + 1
    elif n < x[m]:
      r = m - 1
    else:
      return 1
      break
  return 0

for i in n_lst_s:
  n_lst.append(int(i))
n_lst = mergeSort(n_lst)
for i in m_lst_s:
  print(binSearch(int(i), n_lst))
