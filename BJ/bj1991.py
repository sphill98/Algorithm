N = int(input())

lst = [[]] * 26

for i in range(N):
    x, y, z = input().split()
    lst[ord(x)-65] = [y, z]

def preOrder(n):
    ans = n
    for s in lst[ord(n) - 65]:
        if s != '.':
            ans += preOrder(s)
    return ans

def inOrder(n):
    ans = ''
    if lst[ord(n)-65][0] != '.':
        ans += inOrder(lst[ord(n)-65][0])
    ans += n
    if lst[ord(n)-65][1] != '.':
        ans += inOrder(lst[ord(n)-65][1])
    return ans

def postOrder(n):
    ans = ''
    for s in lst[ord(n) - 65]:
        if s != '.':
            ans += postOrder(s)
    ans += n
    return ans

print(preOrder('A'))
print(inOrder('A'))
print(postOrder('A'))
