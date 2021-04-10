import sys

def paperCut(p): #재귀함수
  s = 0
  for i in p:
    s += sum(i)
  if s == 0:
    return 'w'
  elif s == (len(p) ** 2):
    return 'b'
  else: #색종이를 4개로 나누어 분할정복한다.
    p1, p2, p3, p4 = [], [], [], []
    for i in range(len(p) // 2):
      p1.append(p[i][:(len(p)//2)])
      p2.append(p[i][(len(p)//2):])
      p3.append(p[i+(len(p)//2)][:(len(p)//2)])
      p4.append(p[i+(len(p)//2)][(len(p)//2):])
    return paperCut(p1) + paperCut(p2) + paperCut(p3) + paperCut(p4) #스트링으로 이어줌.

N = int(input())
paper = []
for i in range(N):
  lst = sys.stdin.readline().split()
  n_lst = []
  for s in lst:
    n_lst.append(int(s))
  paper.append(n_lst)

colors = paperCut(paper)
print(colors.count('w'))
print(colors.count('b'))
