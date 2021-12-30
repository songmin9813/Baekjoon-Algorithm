import sys
import heapq
def dijk(board,n,start):
    dist=[2<<30 for _ in range(n+1)]
    dist[start]=0
    q=[]
    heapq.heappush(q,[dist[start],start])
    while q:
        currentd,cnode=heapq.heappop(q)
        if dist[cnode]<currentd:
            continue
        for value in board[cnode]:
            cost=currentd+value[0]
            if cost<dist[value[1]]:
                dist[value[1]]=cost
                heapq.heappush(q,[cost,value[1]])
    return dist
n,e=map(int,sys.stdin.readline().split())
board=[[]for _ in range(n+1)]
for _ in range(e):
    x,y,d=map(int,sys.stdin.readline().split())
    board[x].append([d,y])
    board[y].append([d,x])
start,end=map(int,sys.stdin.readline().split())
result=[dijk(board,n,1),dijk(board,n,start),dijk(board,n,end)]
result=min((result[0][start]+result[1][end]+result[2][n]),(result[0][end]+result[2][start]+result[1][n]))
print(-1) if result>=(2<<30) else print(result)