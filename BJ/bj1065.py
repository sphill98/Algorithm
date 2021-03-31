#브루트포스 알고리즘

def dcha(d_lst, d):
    for i in range(1, len(d_lst)-1):
        if d_lst[i]-d_lst[i+1] != d:
            return False
    return True

def hanSu(a):
    if a < 100:
        return True
    else:
        dig_lst = []
        a_str = str(a)
        for i in a_str:
            dig_lst.append(int(i))
        d = dig_lst[0]-dig_lst[1]
        return dcha(dig_lst, d)
            
n = int(input())

counter = 0

for i in range(1, n+1):
    if hanSu(i):
        counter = counter+1

print(counter)
