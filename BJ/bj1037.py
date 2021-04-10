n = int(input())

s_lst = input().split()
lst = []

for i in s_lst:
    lst.append(int(i))
lst.sort()

print(lst[0]*lst[-1])
