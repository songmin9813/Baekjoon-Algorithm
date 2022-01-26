import sys
import heapq
#mst의 성질의 확장 -> 각 노드간의 거리는 인접해야만 한다 -> 각 좌표별 인접 노드 2개씩만 따오고 비교하면 최소 간선이 보장됨
def prim():
    visited={i:False for i in range(n)}
    visited[0]=True
    Tcount=1
    queue=[]
    for dist,y in edges[0]:
        heapq.heappush(queue,[dist,y])
    while Tcount!=n:
        ldist,ly=heapq.heappop(queue)
        if not visited[ly]:
            global result
            visited[ly]=True
            result+=ldist
            Tcount+=1
            for ndist,ny in edges[ly]:
                if not visited[ny]:
                    heapq.heappush(queue,[ndist,ny])
result=0
n=int(sys.stdin.readline())
planets=[list(map(int,sys.stdin.readline().split()))+[i]for i in range(n)]
edges=[[]for _ in range(n)]
for i1 in range(3):
    planets.sort(key=lambda x:x[i1])
    for i2 in range(0,n-1):
        edges[planets[i2][3]].append([planets[i2+1][i1]-planets[i2][i1],planets[i2+1][3]])
        edges[planets[i2+1][3]].append([planets[i2+1][i1]-planets[i2][i1],planets[i2][3]])
prim()
print(result)