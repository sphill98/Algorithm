import sys

N = int(sys.stdin.readline())

timetable = []

for i in range(N):
    timetable.append(tuple(map(int, sys.stdin.readline().split()))) 
    
timetable.sort(key=lambda x : (x[1], x[0])) #가장 빨리 끝나는 순서대로 정렬한다. 다만, 가장 빨리 끝나는 것 중에서는 빨리 시작하는 것을 우선순위에 놓는다.

conf_lst = [timetable[0]] #가장 빨리 시작하는 것부터 시작.
end_time = timetable[0][1]

for i in range(1, len(timetable)):
    if timetable[i][0] >= end_time:  #현재 회의가 끝나는 시각보다 다음 회의 시작 시간이 늦거나 같다면 해당 회의를 진행한다. 이미 정렬은 된 상태이기 때문에 현재 상태에선 최선의 선택이다.
        conf_lst.append(timetable[i])
        end_time = timetable[i][1]
        
print(len(conf_lst))
