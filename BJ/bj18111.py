import sys

N, M, B = map(int, sys.stdin.readline().split())

mc = []

for i in range(N):
    mc += list(map(int, sys.stdin.readline().split())) #1차원 배열 작성. 반복문 중첩되는 게 보기 싫었다.
    
max_t, max_h = N*M*256*2, 257

for i in range(257): #모든 가능한 높이에 대해 돌려본다.
    m_cnt = 0 #제거할 블록의 수
    p_cnt = 0 #쌓을 블록의 수
    
    for j in range(len(mc)):
        if (mc[j] < i):
            p_cnt += (i-mc[j]) #블록 쌓기
        else:
            m_cnt += (mc[j]-i) #블록 제거
    time = p_cnt + (m_cnt * 2)
    if (p_cnt <= m_cnt + B) and (time <= max_t): #제거한 블록 + 원래 있던 블록 >= 새로 쌓은 블록
        max_t = time
        max_h = i
            
        
print (max_t, max_h)
