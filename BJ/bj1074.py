#bj1074
#S1

N, r, c = map(int, input().split())

def Z(N, r, c):
  if N == 1:
    if r == 0:
      if c == 0:
        return 0
      else:
        return 1
    else:
      if c == 0:
        return 2
      else:
        return 3
  else:
    k = (2 ** (N-1))
    if r < k:
      if c < k:
        return Z(N-1, r, c)
      else:
        return (k ** 2) + Z(N-1, r, c - k) 
    else:
      if c < k:
        return (k ** 2)*2 + Z(N-1, r - k, c)
      else:
        return (k ** 2)*3 + Z(N-1, r - k, c - k)

print(Z(N, r, c))
