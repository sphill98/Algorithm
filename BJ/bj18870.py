#bj18870
#S2
#for문을 최대한 안 쓰는 게 핵심.
N = int(input())

lst0 = list(map(int, input().split())) #한 번에 정수 리스트 만드는 법

s0 = set(lst0) #중복을 제거하기 위해 set을 사용.
lst = list(s0)
lst.sort() #새롭게 인덱싱하면 좌표 압축 가능.
dic = {} #index함수 대신 dic 사용. -> index 사용하면 시간초과.
for i in range(len(lst)):
  dic[lst[i]] = i
for s in lst0:
  print(dic[int(s)], end = ' ')
