import sys
import heapq
def dijk():
    global result
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    dist=[[2<<30 for _ in range(n)]for _ in range(n)]
    dist[0][0]=board[0][0]
    queue=[]
    heapq.heappush(queue,[dist[0][0],0,0])
    while queue:
        cdist,x,y=heapq.heappop(queue)
        if dist[x][y]<cdist:
            continue
        for i in range(4):
            newX=dx[i]+x
            newY=dy[i]+y
            if 0<=newX<n and 0<=newY<n:
                cost=cdist+board[newX][newY]
                if cost<dist[newX][newY]:
                    dist[newX][newY]=cost
                    heapq.heappush(queue,[cost,newX,newY])
    return dist
i=1
while True:
    n=int(sys.stdin.readline())
    if n==0:
        break
    board=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
    result=dijk()
    print("Problem "+str(i)+": "+str(result[n-1][n-1]))
    i+=1