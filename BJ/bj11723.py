import sys

s = [0]*20

M = int(sys.stdin.readline())

for i in range(M):
  ipt = sys.stdin.readline().split()
  if len(ipt) == 1:
    cmd = ipt[0]
  else:
    cmd, x = ipt[0], int(ipt[1])
  if cmd == 'add':
    s[x-1] = 1
  elif cmd == 'remove':
    s[x-1] = 0
  elif cmd == 'check':
    print (s[x-1])
  elif cmd == 'toggle':
    s[x-1] = s[x-1] ^ 1
  elif cmd == 'all':
    s = [1]*20
  elif cmd == 'empty':
    s = [0]*20
