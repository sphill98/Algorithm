#브루트포스 알고리즘

def dcha(d_lst, d):
    for i in range(1, len(d_lst)-1): #안 되는 것 찾을 때까지 찾으면 됨.
        if d_lst[i]-d_lst[i+1] != d: #하나라도 공차랑 다르면 등차수열 성립 x
            return False
    return True

def hanSu(a): #한수 판단 알고리즘.
    if a < 100: #두자리 수는 무조건 한수. 숫자가 두 개니까.
        return True
    else:
        dig_lst = []
        a_str = str(a)
        for i in a_str:
            dig_lst.append(int(i))
        d = dig_lst[0]-dig_lst[1] #공차 설정
        return dcha(dig_lst, d)
            
n = int(input())

counter = 0

for i in range(1, n+1):
    if hanSu(i):
        counter = counter+1

print(counter)
