import sys

def fib(n): #Top-Bottom 다이나믹 프로그래밍
  d = [0]*(n+2) #계산해야하는 수만큼 빈 리스트 생성
  d[0] = [1, 0] #fib(0)의 경우 0 1번 호출, 1 0번 호출
  d[1] = [0, 1] 
  if n >= 2:
    for i in range(2, n+1):
      d[i] = [d[i-1][0] + d[i-2][0], d[i-1][1] + d[i-2][1]] #피보나치 함수
  return d[n]

T = int(input())

for i in range(T):
  n = int(sys.stdin.readline())
  ans = fib(n)
  print(ans[0], ans[1])
