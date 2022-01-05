import sys
from collections import deque
def external():
    result=[[False for _ in range(m)]for _ in range(n)]
    queue=deque()
    result[0][0]=True
    queue.append([0,0])
    while queue:
        cx,cy=queue.popleft()
        dx=[-1,1,0,0]
        dy=[0,0,-1,1]
        for i in range(4):
            newX=dx[i]+cx
            newY=dy[i]+cy
            if 0<=newX<n and 0<=newY<m and not result[newX][newY] and board[newX][newY]==0:
                result[newX][newY]=True
                queue.append([newX,newY])
    return result
def melting(ext):
    flag=False
    for i1 in range(n):
        for i2 in range(m):
            if board[i1][i2]==1:
                count=0
                dx=[-1,1,0,0]
                dy=[0,0,-1,1]
                for i in range(4):
                    newX=dx[i]+i1
                    newY=dy[i]+i2
                    if 0<=newX<n and 0<=newY<m and ext[newX][newY]:
                        count+=1
                if count>=2:#녹는게 생김
                    board[i1][i2]=0
                    flag=True
    return flag
n,m=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split()))for _ in range(n)]
hours=0
while True:
    ext=external()
    if not melting(ext):
        break
    hours+=1
print(hours)