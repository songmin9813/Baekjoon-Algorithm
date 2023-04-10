import sys
def dfs(visited,x,y):
    stack=[[x,y]]
    visited[x][y]=True
    while stack:
        cx,cy=stack.pop()
        dx=[-1,0,1,-1,1,-1,0,1]
        dy=[-1,-1,-1,0,0,1,1,1]
        for i in range(8):
            newX=cx+dx[i]
            newY=cy+dy[i]
            if 0<=newX<n and 0<=newY<m and not visited[newX][newY]:
                visited[newX][newY]=True
                stack.append([newX,newY])

while True:
    result=0
    m,n=map(int, sys.stdin.readline().split())
    if n==0 and m==0:
        break
    board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    visited=[[False for _ in range(m)]for _ in range(n)]
    x,y=0,0
    for i1 in range(n):
        for i2 in range(m):
            if board[i1][i2]==0:
                visited[i1][i2]=True
    for i1 in range(n):
        for i2 in range(m):
            if not visited[i1][i2]:
                dfs(visited, i1, i2)
                result+=1
    print(result)

