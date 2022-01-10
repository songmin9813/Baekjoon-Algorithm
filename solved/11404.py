import sys
import heapq
def dijk(start):
    dist=[2<<30 for _ in range(n+1)]
    dist[start]=0
    q=[]
    heapq.heappush(q,[0,start])
    while q:
        cd,nextnode=heapq.heappop(q)
        if dist[nextnode]<cd:
            continue
        for d,y in board[nextnode]:
            newdist=d+cd
            if newdist<dist[y]:
                dist[y]=newdist
                heapq.heappush(q,[newdist, y])
    return dist
n=int(sys.stdin.readline())
board=[[]for _ in range(n+1)]
result=[]
m=int(sys.stdin.readline())
for _ in range(m):
    x,y,d=map(int, sys.stdin.readline().split())
    board[x].append([d,y])
for i in range(1,n+1):
    row=dijk(i)
    for i in range(1,n+1):
        string='\n' if i==n else ' '
        print(row[i],end=string) if row[i]!=2<<30 else print(0,end=string)