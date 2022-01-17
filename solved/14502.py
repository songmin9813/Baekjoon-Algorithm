import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
zero,virus=[],[]
def bfs(zindex):
    count=len(zero)-3
    visited=[[False for _ in range(m)]for _ in range(n)]
    for i in zindex:
        x,y=zero[i]
        visited[x][y]=True
    queue=deque()
    for v in virus:
        queue.append(v)
        visited[v[0]][v[1]]=True
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        cx,cy=queue.popleft()
        for i in range(4):
            newX,newY=cx+dx[i],cy+dy[i]
            if 0<=newX<n and 0<=newY<m and not visited[newX][newY] and board[newX][newY]==0:
                count-=1
                queue.append([newX,newY])
                visited[newX][newY]=True
    return count
for i1,row in enumerate(board):
    for i2,value in enumerate(row):
        if value==0:
            zero.append([i1,i2])
        elif value==2:
            virus.append([i1,i2])
result=0
for i1 in range(0,len(zero)-2):
    stack=[[i1]]
    while stack:
        cindex=stack.pop()
        if len(cindex)==3:
            result=max(result,bfs(cindex))
            continue
        for i2 in range(cindex[-1]+1,len(zero)):
            tmp=cindex.copy()
            tmp.append(i2)
            stack.append(tmp)
print(result)