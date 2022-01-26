from re import A
import sys
import heapq
#초기 노드 선택-T와 not T 사이의 간선 중 가중치가 가장 작은(최소힙) 노드를 찾아주는 프로그램
def prim(planets):
    visited[0]=True
    queue=[]
    Tcount=1#모든 노드가 T로 들어왔는지 확인하는 변수
    for i in range(1,n):#초기값 힙에 저장하는 과정
        x=planets[i][0]-planets[0][0]
        y=planets[i][1]-planets[0][1]
        heapq.heappush(queue,[(x*x+y*y)**0.5,i])
    while Tcount!=n:
        ldist, li=heapq.heappop(queue)
        if not visited[li]:
            global result
            visited[li]=True
            Tcount+=1
            result+=ldist
            for i in range(n):
                if i==y or visited[i]:
                    continue
                x=abs(planets[i][0]-planets[li][0])
                y=abs(planets[i][1]-planets[li][1])
                heapq.heappush(queue,[(x*x+y*y)**0.5,i])
result=0
n=int(sys.stdin.readline())
planets=[list(map(float, sys.stdin.readline().split()))for _ in range(n)]
visited={i:False for i in range(n)}
prim(planets)
print(result)