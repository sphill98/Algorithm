from collections import deque

#Variables
N, K = map(int, input().split())

dp = [0]*100001 #층수 따지는 리스트. 메모리 초과를 방지하기 위함.

def BFS(n, t):
    queue = deque()
    queue.append(n)
    while queue: #queue가 빌 때까지 진행
        m = queue.popleft() #가장 첫번째 꺼내서
        if m == t:
            return dp[m]
        lst = [m - 1, m + 1, 2 * m] #이동하는 방법을 새로운 노드로 잡는다.
        for i in lst:
            if 0 <= i < 100001 and dp[i] == 0: #메모리 초과 방지. 순서에 유의할 것. dp[i] == 0이 뒤로 와야한다. 안 그러면 i >= 100001인 경우 에러.
                queue.append(i)
                dp[i] = dp[m] + 1
print(BFS(N, K))
