import sys
def dfs(x,y,depth):
    global result
    result=max(result,depth)
    for i in range(4):
        newX=dx[i]+x
        newY=dy[i]+y
        if 0<=newX<n and 0<=newY<m and not visited[board[newX][newY]]:
            visited[board[newX][newY]]=True
            dfs(newX,newY,depth+1)
            visited[board[newX][newY]]=False
n,m=map(int,sys.stdin.readline().split())
dx,dy,result=[-1,1,0,0],[0,0,-1,1],0
board=[list(map(lambda x:ord(x)-65,sys.stdin.readline().rstrip()))for _ in range(n)]
visited={i:False for i in range(27)}
visited[board[0][0]]=True
dfs(0,0,1)
print(result)