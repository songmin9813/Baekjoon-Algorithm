import sys
import heapq
def dijk(board, n, start):
    q=[]
    dist=[2<<30 for _ in range(n+1)]
    dist[start]=0
    heapq.heappush(q,[0,start])
    while q:
        d,nextnode=heapq.heappop(q)
        if dist[nextnode]<d:
            continue
        for value in board[nextnode]:
            cost=d+value[0]
            if cost<dist[value[1]]:
                dist[value[1]]=cost
                heapq.heappush(q,[cost,value[1]])
    return dist
n=int(sys.stdin.readline())
board=[[]for _ in range(n+1)]
m=int(sys.stdin.readline())
for _ in range(m):
    x,y,d=map(int,sys.stdin.readline().split())
    board[x].append([d,y])
start,end=map(int,sys.stdin.readline().split())
print(dijk(board,n,start)[end])