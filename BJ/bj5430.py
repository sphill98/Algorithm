from collections import deque

T = int(input())

def AC(comm, lst):
    flag = True #뒤집혔는지 체크
    for c in comm:
        if c == 'R':
            flag = not flag #Reverse 해준다.
        if c == 'D':
            if len(lst) == 0:
                return ('error') #에러 체크
            if flag: #에러가 아니면 앞에서 빼준다.
                lst.popleft()
            else: #Reverse 됐으니까 뒤에서 빼준다.
                lst.pop()
    if not flag:
        lst.reverse() #Reverse 연산은 한 번만.
    ans = '[' + ','.join(list(lst)) + ']'
    return ans



for _ in range(T):
    command = list(input())
    size = int(input())
    inp_lst = list(input().lstrip('[').rstrip(']').split(','))
    if size == 0:
        lst = deque()
    else:
        lst = deque(inp_lst)
    print(AC(command, lst))
