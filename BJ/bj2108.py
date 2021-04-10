import sys
from collections import Counter

def mode(nums): #최빈값이 여러개면 두번째로 작은 값 출력하래서 만든 건데. 덕분에 빡셈.
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()    
    
    if len(nums) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod

N = int(sys.stdin.readline())

lst = []

for i in range(N):
  lst.append(int(sys.stdin.readline()))

lst.sort()

print(round(sum(lst)/len(lst))) #산술평균. 소수점 이하 첫째 자리에서 반올림.
print(lst[(len(lst)-1) // 2]) #중앙값.
print(mode(lst)) #최빈값.
print(lst[-1] - lst[0]) #범위
