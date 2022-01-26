import sys
import heapq
n,k=map(int, sys.stdin.readline().split())
jems=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
backpack=[int(sys.stdin.readline())for _ in range(k)]
capjems=[]
for v in jems:
    heapq.heappush(capjems,v)
bagqueue=[]
for v in backpack:
    heapq.heappush(bagqueue,v)
count,result,jems=k,0,[]
while bagqueue:
    back=heapq.heappop(bagqueue)
    while capjems and capjems[0][0]<=back:
        weight,value=heapq.heappop(capjems)
        heapq.heappush(jems, [-value,weight])
    if len(jems)==0:
        continue
    else:
        value,weight=heapq.heappop(jems)
        result+=(-value)
    #각 검사가 끝날때마다 사용한 값을 다시 원래대로 돌려놓지 않아도 된다.
    #이미 bag이 크기 순으로 정렬되어있기 때문에 다음에도 다시 들어갈 값이기 때문
print(result)