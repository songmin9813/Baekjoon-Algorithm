import sys
import heapq
def dijk(start):
    queue=[]
    dist=[2<<30 for _ in range(n+2)]
    route=[[]for _ in range(n+2)]
    heapq.heappush(queue,[0,start,[start]])
    while queue:
        cd,cnode,croute=heapq.heappop(queue)
        if dist[cnode]<cd:
            continue
        for nextNode in board[cnode]:
            newdist=nextNode[0]+cd
            if newdist<dist[nextNode[1]]:
                dist[nextNode[1]]=newdist
                copyroute=croute.copy()
                copyroute.append(nextNode[1])
                route[nextNode[1]]=copyroute
                heapq.heappush(queue,[newdist,nextNode[1],copyroute])
    return dist,route
n=int(sys.stdin.readline())
board=[[]for _ in range(n+2)]
m=int(sys.stdin.readline())
for _ in range(m):
    x,y,d=map(int,sys.stdin.readline().split())
    board[x].append([d,y])
x,y=map(int,sys.stdin.readline().split())
rdist,rroute=dijk(x)
print(rdist[y])
print(len(rroute[y]))
for v in rroute[y]:
    print(v, end=' ')