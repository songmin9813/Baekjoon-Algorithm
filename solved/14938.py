import sys
import heapq
def dijk(start):
    result=values[start]
    dist=[2<<30 for _ in range(n+1)]
    dist[start]=0
    queue=[]
    heapq.heappush(queue,[dist[start],start])
    while queue:
        cdist,cnode=heapq.heappop(queue)
        if dist[cnode]<cdist:
            continue
        for value in nodes[cnode]:
            cost=cdist+value[0]
            if cost<dist[value[1]]:
                dist[value[1]]=cost
                heapq.heappush(queue,[cost,value[1]])
    return dist
n,m,r=map(int,sys.stdin.readline().split())
values=[0]+list(map(int,sys.stdin.readline().split()))
nodes=[[]for _ in range(n+2)]
for _ in range(r):
    x,y,d=map(int,sys.stdin.readline().split())
    nodes[x].append([d,y])
    nodes[y].append([d,x])
result=0
for i in range(1,n+1):
    dist=dijk(i)
    tmpresult=0
    for i,v in enumerate(dist):
        if v<=m:
            tmpresult+=values[i]
    result=max(result,tmpresult)
print(result)