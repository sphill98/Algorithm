import sys

N = int(input())

max_h = []

def push(x): #추가 알고리즘
  max_h.append(x) #새로운 원소는 기본적으로 맨 뒤에 넣는다
  p = len(max_h) - 1 #맨 마지막 노드부터 정렬 시작
  while True:
    if p == 0: #노드가 루트로 오면 종료
      break
    elif max_h[p] >= max_h[(p-1) // 2]: # 부모 노드와 값 비교. 1, 2의 부모가 0 => p-1 // 2
      tmp = max_h[(p-1)//2]
      max_h[(p-1)//2] = max_h[p]
      max_h[p] = tmp
      p = (p-1) // 2
    else: #더 이상 노드가 올라가지 못하면 종료
      break

def check(): #삭제 알고리즘
  if len(max_h) == 0: #힙이 비어있으면 0을 리턴
    return 0
  me = max_h[0] #최대 원소를 임시 변수에 넣는다.
  max_h[0] = max_h[-1] #루트 지점을 힙의 마지막 원소로 대체
  max_h.pop() #힙의 마지막 원소 삭제
  p = 0 #루트부터 정렬 시작.
  while True:
    if (2*p)+2 > len(max_h): #더 이상 자식 노드가 없으면 종료
      break
    elif (2*p+2) == len(max_h): #자식 노드가 한 개인 경우
      if max_h[p] <= max_h[(2*p)+1]: #자식 노드보다 값이 크면 내려간다.
        tmp = max_h[p]
        max_h[p] = max_h[(2*p)+1]
        max_h[(2*p)+1] = tmp
        p = (2*p)+1
      else:
        break
    else: #자식 노드가 두 개인 경우 최소 원소와 자리를 바꾼다.
      if max_h[p] <= max_h[(2*p)+1] and max_h[(2*p)+2] <= max_h[(2*p)+1]:
        tmp = max_h[p]
        max_h[p] = max_h[(2*p)+1]
        max_h[(2*p)+1] = tmp
        p = (2*p)+1
      elif max_h[p] <= max_h[(2*p)+2] and max_h[(2*p)+1] <= max_h[(2*p)+2]:
        tmp = max_h[p]
        max_h[p] = max_h[(2*p)+2]
        max_h[(2*p)+2] = tmp
        p = (2*p)+2
      else:
        break
  return me
  
for i in range(N):
  x = int(sys.stdin.readline())
  if x != 0:
    push(x)
  else:
    print(check())  
