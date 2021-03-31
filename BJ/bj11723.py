import sys

s = [0]*20

M = int(sys.stdin.readline())

for i in range(M):
  cmd = sys.stdin.readline().split()
  if cmd[0] == 'add':
    k = int(cmd[1])
    s[k-1] = 1
  elif cmd[0] == 'remove':
    k = int(cmd[1])
    s[k-1] = 0
  elif cmd[0] == 'check':
    k = int(cmd[1])
    print (s[k-1])
  elif cmd[0] == 'toggle':
    k = int(cmd[1])
    s[k-1] = s[k-1] ^ 1
  elif cmd[0] == 'all':
    s = [1]*20
  elif cmd[0] == 'empty':
    s = [0]*20
