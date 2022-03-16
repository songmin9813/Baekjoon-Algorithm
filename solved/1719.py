import sys
import heapq
def dijk(start):
    dist=[2<<30 for _ in range(n+1)]
    dist[start]=0
    firstR=[0 for _ in range(n+1)]
    queue=[[0,start]]
    while queue:
        cdist,cx=heapq.heappop(queue)
        if cdist>dist[cx]:
            continue
        for ndist,ny in nodes[cx]:
            newdist=ndist+cdist
            if dist[ny]>newdist:
                dist[ny]=newdist
                heapq.heappush(queue,[newdist,ny])
                if cx==start:
                    firstR[ny]=ny
                else:
                    firstR[ny]=firstR[cx]
    return firstR

n,m=map(int,sys.stdin.readline().split())
nodes=[[]for _ in range(n+1)]
for _ in range(m):
    x,y,d=map(int,sys.stdin.readline().split())
    nodes[x].append([d,y])
    nodes[y].append([d,x])
result=[]
for i in range(1,n+1):
    result.append(dijk(i))
for i1 in range(n):
    for i2 in range(1,n+1):
        string='\n' if i2==n else ' '
        if result[i1][i2]==0:
            print('-', end=string)
        else:
            print(result[i1][i2],end=string)