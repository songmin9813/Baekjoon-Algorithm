import sys
from collections import deque
def bfs(x,y):
    visited = [[False for _ in range(m)]for _ in range(n)]
    queue=deque()
    queue.append([x,y])
    visited[x][y]=True
    result[x][y]=0
    dx=[-1,0,0,1]
    dy=[0,-1,1,0]
    while queue:
        cx,cy=queue.popleft()
        for i in range(4):
            newX,newY=cx+dx[i],cy+dy[i]
            if 0<=newX<n and 0<=newY<m and not visited[newX][newY] and board[newX][newY]!=0:
                queue.append([newX,newY])
                result[newX][newY]=result[cx][cy]+1
                visited[newX][newY]=True
                
n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
result=[[-1 for _ in range(m)]for _ in range(n)]
x,y=-1,-1
for i1 in range(n):
    for i2 in range(m):
        if board[i1][i2]==0:
            result[i1][i2]=0
        elif board[i1][i2]==2:
            x,y=i1,i2
bfs(x,y)
for value in result:
    print(*value)