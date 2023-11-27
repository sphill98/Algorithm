import sys

input = sys.stdin.readline

T = int(input())

MBTI = {'INFP':0b0000, 'INFJ':0b0001, 'INTP':0b0010, 'INTJ':0b0011, 'ISFP':0b0100, 'ISFJ':0b0101, 'ISTP':0b0110, 'ISTJ':0b0111,
        'ENFP':0b1000, 'ENFJ':0b1001, 'ENTP':0b1010, 'ENTJ':0b1011, 'ESFP':0b1100, 'ESFJ':0b1101, 'ESTP':0b1110, 'ESTJ':0b1111}

def distMBTI(m1, m2, m3):
    return (bin(MBTI[m1] ^ MBTI[m2]) + bin(MBTI[m2] ^ MBTI[m3]) + bin(MBTI[m3] ^ MBTI[m1])).count('1') #XOR 연산 활용

for _ in range(T):
    N = int(input())
    lst = list(input().split())
    min_ = 45
    if N > 32: #비둘기집의 원리 활용. 32보다 많아지면 무조건 0
        print(0)
    else:
        for i in range(N):
            for j in range(i + 1, N):
                for k in range(j + 1, N):
                    tmp = distMBTI(lst[i], lst[j], lst[k])
                    if tmp <= min_:
                        min_ = tmp
        print(min_)
    
