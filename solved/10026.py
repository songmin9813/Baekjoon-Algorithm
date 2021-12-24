from collections import deque
def bfs(board,queue,flag,string,n):
    while queue:
        i1,i2,currentnode=queue.popleft()
        dx=[-1,0,0,1]
        dy=[0,1,-1,0]
        for i in range(4):
            newX=i1+dx[i]
            newY=i2+dy[i]
            if flag is True:#적록색약이 아님
                if 0<=newX<n and 0<=newY<n and visited[newX][newY] is not True and board[newX][newY]==currentnode:
                    visited[newX][newY]=True
                    queue.append([newX,newY,board[newX][newY]])
            else:#적록색약
                if 0<=newX<n and 0<=newY<n and visited[newX][newY] is not True:
                    if (currentnode=='R' and (board[newX][newY]==currentnode or board[newX][newY]=='G'))or(currentnode=='G' and (board[newX][newY]==currentnode or board[newX][newY]=='R'))or(currentnode!='R' and currentnode!='G' and board[newX][newY]==currentnode):
                        visited[newX][newY]=True
                        queue.append([newX,newY,board[newX][newY]])                    
n=int(input())
board=[list(input()) for _ in range(n)]
queue=deque()
visited=[[False for col in range(n)] for row in range(n)]
onecount=0
for i1,row in enumerate(board):
    for i2,value in enumerate(row):
        if visited[i1][i2] is not True:
            visited[i1][i2]=True
            onecount+=1
            queue.append([i1,i2,value])
            bfs(board,queue,True,value,n)
queue.clear()
visited=[[False for col in range(n)] for row in range(n)]
twocount=0
for i1,row in enumerate(board):
    for i2,value in enumerate(row):
        if visited[i1][i2] is not True:
            visited[i1][i2]=True
            twocount+=1
            queue.append([i1,i2,value])
            bfs(board,queue,False,value,n)
print(str(onecount)+' '+str(twocount))